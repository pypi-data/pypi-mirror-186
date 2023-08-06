"""Implements an interface for backtesting."""

# Python
import datetime
import json
import os
from math import pi, cos, sin 
import collections, functools, operator

import pprint as pprint
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import bson
from IPython.display import display, clear_output
from ipywidgets import FloatProgress
from pymongo import MongoClient

# Gaius Agent
from ia.gaius.agent_client import AgentClient
from ia.gaius.prediction_models import *
from ia.gaius import data_ops
from ia.gaius.data_ops import Data
from ia.gaius.tests import classification, utility

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

import pandas as pd 
from sklearn.metrics import accuracy_score
   
# Data
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import accuracy_score

class BackTest:
    """Provides an interface for backtesting."""
    def __init__(self, **kwargs):
        """
        Pass this a configuration dictionary as the argument such as:

        test_results_database = 'mongodb://mongo-kb:27017'

        test_config = {'name':'backtest-classification',
                        'test_type': 'classification', ## 'classification' or 'utility'
                        'utype': None, ## If 'test_type' = 'utility', then set to either 'polarity' or 'value'
                        'shuffle_data': True,
                        'fresh_start_memory': True, ## Clear all memory when starting and between runs
                        'mongo_location': test_results_database, ## location of mongo db where test results will be stored
                        'learning_strategy': 'continuous', # None, 'continuous' or 'on_error'
                        'bottle': bottle,
                        'data_source': dataset, ## or provide 'data_directories' as iterable of data.
                        'percent_reserved_for_training': 20,
                        'percent_of_dataset_chosen': 100,
                        'total_test_counts': 1 }

        test = BackTest(**test_config)

        mongo_location provides the location of a mongo database where the test results will be stored.

        Option of either data_source or data_directories can be provided:

            data_source provided is a sequence of sequences of GDF objects.
            data_directories provided should be a list of directories containing files of GDF as json dumps.

        """
        self.configuration = kwargs
        self.errors = []
        self.name = str(kwargs['name'])
        self.test_type = kwargs['test_type']
        self.utype = kwargs['utype']
        self.shuffle_data = kwargs['shuffle_data']
        self.learning_strategy = kwargs['learning_strategy']
        self.fresh_start_memory = kwargs['fresh_start_memory']
        self.mongo_location = kwargs['mongo_location']
        self.bottle = kwargs['bottle']
        self.bottle.summarize_for_single_node = False
        if 'data_directories' in self.configuration:
            self.data_directories = kwargs['data_directories']
            self.data_source = None
        elif 'data_source' in self.configuration:
            self.data_source = kwargs['data_source']
            self.configuration['data_source'] = 'from-source'
            self.data_directories = None
        self.percent_reserved_for_training = int(kwargs['percent_reserved_for_training'])
        self.percent_of_dataset_chosen = int(kwargs['percent_of_dataset_chosen'])
        self.total_test_counts = int(kwargs['total_test_counts'])
        self.current_test_count = 0

        self.mongo_client = MongoClient(self.mongo_location)  # , document_class=OrderedDict)
        # Collection storing the backtesting results is the bottle's name.
        self.mongo_client.backtesting = self.mongo_client['{}-{}-{}'.format(
            self.name, self.bottle.genome.agent, self.bottle.name)]
        self.test_configuration = self.mongo_client.backtesting.test_configuration
        self.test_status = self.mongo_client.backtesting.test_status
        self.test_errors = self.mongo_client.backtesting.test_errors
        self.backtesting_log = self.mongo_client.backtesting.backtesting_log
        self.interrupt_status = self.mongo_client.backtesting.interrupt_status

        if self.test_type == "utility":
            self._tester = utility.Tester(**kwargs)
        elif self.test_type == 'classification':
            self._tester = classification.Tester(**kwargs)

        if self.data_directories:
            self.data = Data(data_directories=self.data_directories)
        elif self.data_source:
            self.data = Data(dataset=self.data_source)
        self.data.prep(self.percent_of_dataset_chosen, self.percent_reserved_for_training, shuffle=self.shuffle_data)
        sequence_count = len(self.data.train_sequences) + len(self.data.test_sequences)

        self.number_of_things_to_do = self.total_test_counts * sequence_count
        self.number_of_things_done = 0
        self.status = "not started"

        self.interrupt_status.replace_one({}, {'interrupt': False}, upsert=True)
        self.test_status.replace_one({}, {'status': 'not started',
                                          'number_of_things_to_do': self.total_test_counts * sequence_count,
                                          'number_of_things_done': 0,
                                          'current_test_count': self.current_test_count
                                          }, upsert=True)

        self.test_errors.drop()
        self.backtesting_log.drop()
        self.backtesting_log.insert_one({"timestamp_utc": datetime.datetime.utcnow(), "status": "test-started"})

        self.test_configuration.drop()
        self.test_configuration.insert_one({
            'name': self.name,
            'test_type': self.test_type,
            'utype': self.utype,
            'shuffle_data': self.shuffle_data,
            'learning_strategy': self.learning_strategy,
            'fresh_start_memory': self.fresh_start_memory,
            "bottle_name": self.bottle.name,
            "agent": self.bottle.genome.agent,
            "ingress_nodes": self.bottle.ingress_nodes,
            "query_nodes": self.bottle.query_nodes
        })

        headers = ["Test Run", "Trial", "Phase", "Filename", "Historical"] + [node["name"] for node in
                                                                              self.bottle.query_nodes] + ["hive"]
        self.backtesting_log.insert_one({"headers": headers})
        self.progress = FloatProgress(min=0, max=self.number_of_things_to_do, description="Starting...", bar_style="info")

        print("Recording results at '%s-%s-%s'" % (self.name, self.bottle.genome.agent, self.bottle.name))

    def _reset_test(self):
        """Reset the instance to the state it was in when created."""
        self.backtesting_log.insert_one({"timestamp_utc": datetime.datetime.utcnow(), "status": "resetTest"})
        if self.data_directories:
            self.data = Data(data_directories=self.data_directories)
        elif self.data_source:
            self.data = Data(dataset=self.data_source)
        self.data.prep(self.percent_of_dataset_chosen, self.percent_reserved_for_training, shuffle=self.shuffle_data)
        self._tester.next_test_prep()

    def _end_test(self):
        """Called when the test ends."""
        self.status = "finished"
        self.backtesting_log.insert_one({"timestamp_utc": datetime.datetime.utcnow(), "status": "test-ended"})
        nodes_status = self.bottle.show_status()
        self.test_status.replace_one({}, {'status': 'finished',
                                          'nodes_status': nodes_status,
                                          'number_of_things_to_do': self.number_of_things_to_do,
                                          'number_of_things_done': self.number_of_things_to_do,
                                          'current_test_count': self.current_test_count}, upsert=True)

    def run(self):
        display(self.progress)
        self.backtesting_log.insert_one({"timestamp_utc": datetime.datetime.utcnow(), "status": "run"})
        while self.current_test_count < self.total_test_counts:
            self.current_test_count += 1
            self._setup_training()
            for sequence in self.data.train_sequences:
                self._train(sequence)
                self.number_of_things_done += 1
                self.progress.value = self.number_of_things_done
                self.progress.description = '%0.2f%%' % (100 * self.number_of_things_done / self.number_of_things_to_do)

            self._setup_testing()
            for sequence in self.data.test_sequences:
                self._test(sequence)
                self.number_of_things_done += 1
                self.progress.value = self.number_of_things_done
                self.progress.description = '%0.2f%%' % (100 * self.number_of_things_done / self.number_of_things_to_do)

            if self.current_test_count < self.total_test_counts:
                self._reset_test()
            else:
                self._end_test()
                clear_output()

    def _setup_training(self):
        """Setup instance for training."""
        self.backtesting_log.insert_one({"timestamp_utc": datetime.datetime.utcnow(), "status": "setupTraining"})
        self.status = "training"
        self.test_status.replace_one({}, {'status': 'training',
                                          'number_of_things_to_do': self.number_of_things_to_do,
                                          'number_of_things_done': self.number_of_things_done,
                                          'current_test_count': self.current_test_count}, upsert=True)
        if self.fresh_start_memory:
            self.bottle.clear_all_memory()
        return 'ready'

    def _train(self, sequence):
        """Train with the sequence in *sequence*."""
        # get a sequence either from a file, or directly as a list:
        if self.data_directories:
            self.backtesting_log.insert_one(
                {"timestamp_utc": datetime.datetime.utcnow(), "status": "training", "file": os.path.basename(sequence)})
            with open(sequence) as f:
                sequence = [json.loads(data.strip()) for data in f if data]
        elif self.data_source:
            sequence = sequence
            self.backtesting_log.insert_one({"timestamp_utc": datetime.datetime.utcnow(), "status": "training"})

        ## Train the sequence:
        result_log_record = self._tester.train(sequence)
        result_log_record['trial'] = self.number_of_things_done
        result_log_record['run'] = self.current_test_count
        self.backtesting_log.insert_one(result_log_record)
        return 'ready'

    def _setup_testing(self):
        """Set up the instance to begin backtesting."""
        self.backtesting_log.insert_one({"timestamp_utc": datetime.datetime.utcnow(), "status": "setupTesting"})
        self.status = "testing"
        self.test_status.replace_one({}, {'status': 'testing',
                                          'number_of_things_to_do': self.number_of_things_to_do,
                                          'number_of_things_done': self.number_of_things_done,
                                          'current_test_count': self.current_test_count}, upsert=True)
        return 'ready'

    def _test(self, sequence):
        """Run the backtest on *sequence*."""
        ## get a sequence either from a file, or directly as a list:
        if self.data_directories:
            self.backtesting_log.insert_one(
                {"timestamp_utc": datetime.datetime.utcnow(), "status": "testing", "file": os.path.basename(sequence)})
            with open(sequence) as f:
                sequence = [json.loads(data.strip()) for data in f if data]
        elif self.data_source:
            sequence = sequence
            self.backtesting_log.insert_one({"timestamp_utc": datetime.datetime.utcnow(), "status": "testing"})

        ## Test the sequence and record the results.
        result_log_record = self._tester.test(sequence)
        result_log_record['trial'] = self.number_of_things_done
        result_log_record['run'] = self.current_test_count
        self.backtesting_log.insert_one(bson.son.SON(result_log_record))
        return 'ready'

def classification_report(back_tester : BackTest): 
    class_values = get_class_distribution(back_tester)

    plot_class_distributions(back_tester, class_values)

    predictor_operator_characteristic(back_tester, class_values)

    fidelity_charts(back_tester)

def get_class_distribution(back_tester : BackTest) -> dict: 
    return_dict = {"training" : {}, "testing" : {}} 
    training_class_labels = [] 
    testing_class_labels = [] 
    if back_tester.data_directories != None: 
        for file in back_tester.data.train_sequences: 
            with open(file) as f: 
                sequence = [json.loads(data.strip()) for data in f if data] 
                if(sequence[-1]["strings"][-1] != ""): 
                    training_class_labels.append(sequence[-1]["strings"][-1])

        for key in set(training_class_labels):
            return_dict["training"][key] = training_class_labels.count(key)


        for file in back_tester.data.test_sequences:
            with open(file) as f:
                sequence = [json.loads(data.strip()) for data in f if data]
                if(sequence[-1]["strings"][-1] != ""):
                    testing_class_labels.append(sequence[-1]["strings"][-1])

        for key in set(testing_class_labels):
            return_dict["testing"][key] = testing_class_labels.count(key)

    else:
        for seq in back_tester.train_sequences:
            if(sequence[-1]["strings"][-1] != ""):
                training_class_labels.append(sequence[-1]["strings"][-1])

        for key in set(training_class_labels):
            return_dict["training"][key] = training_class_labels.count(key)

        for seq in back_tester.test_sequences:
            if(sequence[-1]["strings"][-1] != ""):
                testing_class_labels.append(sequence[-1]["strings"][-1])

        for key in set(testing_class_labels):
            return_dict["testing"][key] = testing_class_labels.count(key)

    return return_dict

def plot_class_distributions(back_tester : BackTest, class_values): 
    # make subplot figure 
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

    # get training data distribution
    x = class_values["training"]
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'class'})

    # add first pie subplot
    fig.add_trace(
        go.Pie(labels=data["class"].to_list(), values=data["value"].to_list(), name="Training", 
               title='Training', texttemplate = "%{label}<br>(%{percent:.2f})"),
        1, 1)

    fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    # get testing data distribution
    x = class_values["testing"]
    data = pd.Series(x).reset_index(name='value').rename(columns={'index': 'class'})

    # add other pie subplot
    fig.add_trace(
        go.Pie(labels=data["class"].to_list(), values=data["value"].to_list(), 
               name="Testing", title='Testing', texttemplate = "%{label}<br>(%{percent:.2f})"),
        1, 2,)

    fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(height=500, width=800, title_text="Historical Class Distributions")
    fig.show()

def predictor_operator_characteristic(back_tester : BackTest, class_values): 
    # create some variables to hold data 
    predicted_labels = [] 
    true_labels = [] 
    num_correct = 0 
    num_wrong = 0

    # go through results and record number of correct and incorrect
    for doc in back_tester.backtesting_log.find({"phase" : "testing"}):
        predicted_labels.append(doc['node_predictions']["hive"])
        true_labels.append(doc['historical_expecting'])
        if(doc['historical_expecting'] == doc['node_predictions']["hive"]):
            num_correct += 1
        else:
            num_wrong += 1

    # calculate scores
    accuracy_of_positives = accuracy_score(predicted_labels, true_labels)

    precision_of_positives = num_correct / (num_wrong + num_correct)


    line_color=dict(color="green")

    layout1= go.Layout(title=go.layout.Title(text="Predictor Operator Characteristic",x=0.5),
        xaxis={'title':'Precision of Positives (Positive Predictive Values)','range':[0,1.0]},
        yaxis={'title':'Accuracy of Positives','range':[0,1.0]})

    point_plot=[
      go.Scatter(x=[(1 / len(class_values["testing"].keys())) for i in range(2)],
             y=[i for i in range(2)],
             name="Random Chance",
             legendgroup="Random Chance",
             line=line_color),
        go.Scatter(x = [accuracy_of_positives], y = [precision_of_positives], 
                   name = "GAIUS Performance", legendgroup="GAIUS Performance",
                  marker={"color":"green", "size":25}, mode="markers")
    ]

    go.Figure(data=point_plot, layout=layout1).show()

def fidelity_charts(back_tester : BackTest):
    import collections
    calculated_things = {}
    # get the names of all the nodes, and add hive
    # will probably need to filter some out or not
    nodes = [name["name"] for name in back_tester.bottle.all_nodes]
    nodes.insert(0, "hive")
    # nodes.append("hive")
    
    # set up dictionary, before reading info from backtesting_log
    for node in nodes:
        calculated_things[node] = {}
        calculated_things[node]["node_predictions"] = []
        calculated_things[node]["num_correct"] = 0
        calculated_things[node]["num_wrong"] = 0
        for actual in back_tester.backtesting_log.distinct('historical_expecting'):
            calculated_things[node][actual] = {}
            for predicted in back_tester.backtesting_log.distinct('historical_expecting'):
                calculated_things[node][actual][predicted] = 0
    
    # get information from backesting_log
    for doc in back_tester.backtesting_log.find({"phase" : "testing"}):
        for node in nodes:
            calculated_things[node][doc['historical_expecting']][doc['node_predictions'][node]] += 1
            calculated_things[node]["node_predictions"].append(doc['node_predictions'][node])
            if(doc['historical_expecting'] == doc['node_predictions'][node]):
                calculated_things[node]["num_correct"] += 1
            else:
                calculated_things[node]["num_wrong"] += 1
    
    # get status of bottles
    bottle_statuses = back_tester.bottle.show_status()
    
    # set up suplots
    subplot_spec = []
    subplot_titles = []
    width = 1000
    height = 400 * (len(nodes)+1)
    
    for node in nodes:
        subplot_spec.append([{"type": "table"},
                   {"type": "domain"},
                   {"type": "domain"}])
        
        subplot_titles.append(node.capitalize())
        subplot_titles.append('Fidelity')
        subplot_titles.append("Predicted Class Distributions")
        
    
    subplot_spec.append([{"type": "table", "colspan": 3}, None, None])
    subplot_titles.append("Confusion Matrix")
    
    fig = make_subplots(rows=len(nodes)+1, cols=3,
            specs=subplot_spec,
            subplot_titles=subplot_titles,
            column_widths=[width / 3, width /3, width / 3])
    
    # go through nodes and plot their data
    row_index = 1
    for i, node in enumerate(nodes):
        # make small table with node status
        if(node == "hive"):
            fig.add_trace(go.Table(
                header=dict(values=[node.capitalize() + " Status"],
                    align='left'),
                cells=dict(values=[[""]],
                   align='left')), row_index, 1)
        else:
            fig.add_trace(go.Table(
                header=dict(values=[node],
                    align='left'),
                cells=dict(values=[[str(bottle_statuses[node])]],
                   align='left')), row_index, 1,)
            
        # pie chart for Fidelity
        data = {}
        data["values"] = [calculated_things[node]["num_correct"], calculated_things[node]["num_wrong"]]
        data["angle"] = [val / sum(data["values"]) * 2*pi for val in data["values"]]
        data['percentage'] = [val / sum(data["values"]) * 100 for val in data["values"]]
        data['percentage'] = ['{0:.2f}%'.format(val) for val in data['percentage']]
        data["class"] = ["num_correct", "num_wrong"]
        data['color'] = ["green", "red"]
        
        fig.add_trace(
        go.Pie(labels=data["class"], values=data["values"]), row_index, 2,)
    
#         fig.update_traces(hole=.4, hoverinfo="label+percent+name", selector=dict(type="domain"))

        # pie chart for class distribution
        data = {}
        freqs = dict(collections.Counter(calculated_things[node]["node_predictions"]))
        data["values"] = [val for val in freqs.values()]
        data["class"] = [val for val in freqs.keys()]
        data["angle"] = [val / sum(data["values"]) * 2*pi for val in data["values"]]
        data['percentage'] = [val / sum(data["values"]) * 100 for val in data["values"]]
        data['percentage'] = ['{0:.2f}%'.format(val) for val in data['percentage']]
        
        fig.add_trace(
        go.Pie(labels=data["class"], values=data["values"]), row_index, 3,)
        
        fig.update_traces(hole=.4, hoverinfo="label+percent+name", selector=dict(type="pie"))
        row_index += 1
        
    # make confusion matrix
    classes = data["class"]
    
    data["actual"] = [[val] * 3 for val in classes]
    data["actual"] = [item for sublist in data["actual"] for item in sublist]
    data["predicted"] = [classes] * 3
    data["predicted"] = [item for sublist in data["predicted"] for item in sublist]
        
    # go through all combinations of classes for hive since it would be the final prediction
    # ****can be modified so that each node gets their own confusion matrix****
    data["frequency"] = [calculated_things["hive"][actual][predicted] 
                       for actual, predicted in zip(data["actual"], data["predicted"])]
    data["% of results"] = [calculated_things["hive"][actual][predicted] / 
                       (calculated_things["hive"]["num_correct"] + 
                        calculated_things["hive"]["num_wrong"]) * 100 
                        for actual, predicted in zip(data["actual"], data["predicted"])]
    
    data["% of results"] = ['{0:.2f}%'.format(val) for val in data["% of results"]]
        
    fig.add_trace(go.Table(
            header=dict(values=["Actual", "Predicted", "Frequency", "% of results"],
                align='left'),
            cells=dict(values=[data["actual"], data["predicted"], data["frequency"], data["% of results"]],
                align='left'), ), row_index, 1)
    
    fig.update_layout(height=height, width=width, title_text="Classification Report")
    fig.update_traces(
        cells_font=dict(size = 15),
        selector=dict(type="table"))
    fig.show()
    
class PerformanceValidationTest():
    """
    Performance Validation Test (PVT) - Splits a GDF folder into training and testing sets.
    Based on the test type certain visualizations will be produced.
    Test types:
        - Classification
        - Emotive Value
        - Emotives Polarity
    """
    def __init__(self, agent,ingress_nodes,query_nodes,num_of_tests,ds_filepath,pct_of_ds,results_filepath,
                 pct_res_4_train, test_type, test_prediction_strategy="continuous",
                 clear_all_memory_before_training=True, turn_prediction_off_during_training=False, shuffle=False):
        
        self.agent                               = agent
        self.ingress_nodes                       = ingress_nodes
        self.query_nodes                         = query_nodes
        self.num_of_tests                        = num_of_tests
        self.ds_filepath                         = ds_filepath
        self.results_filepath                    = results_filepath
        self.pct_of_ds                           = pct_of_ds
        self.pct_res_4_train                     = pct_res_4_train
        self.shuffle                             = shuffle
        self.test_type                           = test_type
        self.clear_all_memory_before_training    = clear_all_memory_before_training
        self.turn_prediction_off_during_training = turn_prediction_off_during_training
        self.test_prediction_strategy            = test_prediction_strategy
        self.dataset                             = data_ops.Data(data_directories=[self.ds_filepath]) 
        self.emotives_set                        = None
        self.labels_set                          = None
        self.predictions                         = None
        self.actuals                             = None
        self.emotives_metrics_data_structures    = None
        self.class_metrics_data_structures       = None
        self.metrics_dataframe                   = None
        self.pvt_results                         = None
        
        # Show Agent status by Default
        self.agent.show_status()
        
        # Assign Ingress and Query Nodes
        self.agent.set_ingress_nodes(nodes=self.ingress_nodes)
        self.agent.set_query_nodes(nodes=self.query_nodes)
  
        print(f"num_of_tests      = {self.num_of_tests}\n")
        print(f"ds_filepath       = {self.ds_filepath}\n")
        print(f"pct_of_ds         = {self.pct_of_ds}\n")
        print(f"pct_res_4_train   = {self.pct_res_4_train}\n")
        
        # Setting summarize single to False by default in order to handle multiply nodes topologies
        self.agent.set_summarize_for_single_node(False)
        print(f"summarize_for_single_node status   = {self.agent.summarize_for_single_node}\n")
              
    def prepare_datasets(self):
        self.dataset.prep(
            percent_of_dataset_chosen=self.pct_of_ds,
            percent_reserved_for_training=self.pct_res_4_train,
            shuffle=self.shuffle
        )
        print(f"Length of Training Set = {len(self.dataset.train_sequences)}\n")
        print(f"Length of Testing Set  = {len(self.dataset.test_sequences)}\n")

    
    def conduct_pvt(self):
        """
        Iterate through number of tests the user wants to conduct.
        Driver function.
        """
        # Validate Test Type    
        if self.test_type == 'classification':
            print("Conducting Classification PVT...\n")
            self.pvt_results = {}          
            for test_num in range(0,self.num_of_tests):
                print(f'Conducting Test # {test_num+1}')
                print('\n---------------------\n')
                print("Preparing Training and Testing Datasets...")
                self.prepare_datasets()
                print('\n---------------------\n')
                print("Training Agent...")
                self.train_agent()
                print('\n---------------------\n')
                self.agent.show_status()
                print('\n---------------------\n')
                print("Testing Agent...")
                self.test_agent()
                print('\n---------------------\n')
                self.agent.show_status()
                print('\n---------------------\n')
                print('Getting Classification Metrics...')
                self.get_classification_metrics()
                print('Saving results to pvt_results...')
                self.pvt_results[f'test_num_{test_num+1}_metrics'] = self.class_metrics_data_structures
                self.pvt_results[f'test_num_{test_num+1}_metrics'] = self.update_test_results_w_hive_classification_metrics(self.pvt_results[f'test_num_{test_num+1}_metrics'])
                print('\n---------------------\n')
                print('Plotting Results...')
                self.plot_confusion_matrix(test_num=test_num+1)
                print('\n---------------------\n')
        elif self.test_type == 'emotives_value':
            print("Conducting Emotives Value PVT...\n")
            self.pvt_results = {}
            for test_num in range(0,self.num_of_tests):
                print(f'Conducting Test # {test_num+1}')
                print('\n---------------------\n')
                print("Preparing Training and Testing Datasets...")
                self.prepare_datasets()
                print('\n---------------------\n')
                print("Training Agent...")
                self.train_agent()
                print('\n---------------------\n')
                self.agent.show_status()
                print('\n---------------------\n')
                print("Testing Agent...")
                self.test_agent()
                print('\n---------------------\n')
                self.agent.show_status()
                print('\n---------------------\n')
                print('Getting Emotives Value Metrics...')
                self.get_emotives_value_metrics()
                print('Saving results to pvt_results...')
                self.pvt_results[f'test_num_{test_num+1}_metrics'] = self.emotives_metrics_data_structures
                self.pvt_results[f'test_num_{test_num+1}_metrics'] = self.update_test_results_w_hive_emotives_value_metrics(self.pvt_results[f'test_num_{test_num+1}_metrics'])
                print('\n---------------------\n')
                print('Plotting Results...')
                self.plot_emotives_value_charts(test_num=test_num)
                print('\n---------------------\n')
        elif self.test_type == 'emotives_polarity':
            print("Conducting Emotives Polarity PVT...\n")
            self.pvt_results = {}
            for test_num in range(0,self.num_of_tests):
                print(f'Conducting Test # {test_num+1}')
                print('\n---------------------\n')
                print("Preparing Training and Testing Datasets...")
                self.prepare_datasets()
                print('\n---------------------\n')
                print("Training Agent...")
                self.train_agent()
                print('\n---------------------\n')
                self.agent.show_status()
                print('\n---------------------\n')
                print("Testing Agent...")
                self.test_agent()
                print('\n---------------------\n')
                self.agent.show_status()
                print('Getting Emotives Polarity Metrics...')
                self.get_emotives_polarity_metrics()
                print('Saving results to pvt_results...')
                self.pvt_results[f'test_num_{test_num+1}_metrics'] = self.emotives_metrics_data_structures
                self.pvt_results[f'test_num_{test_num+1}_metrics'] = self.update_test_results_w_hive_emotives_polarity_metrics(self.pvt_results[f'test_num_{test_num+1}_metrics'])

        else:
            raise Exception(
                """
                Please choose one of the test type:
                  - classification
                  - emotives_value
                  - emotives_polarity
                  
                ex.
                --> pvt.test_type='emotives_value'
                
                then, retry
                
                --> pvt.conduct_pvt()
                """
            )        

         
    def train_agent(self):
        """
        Takes a training set of gdf files, and then trains an agent on those records.
        The user can turn prediction off if the topology doesn't have abstractions
        where prediction is needed to propagate data through the topology.
        """
        # Initialize
        if self.clear_all_memory_before_training==True:
            print('Clearing memory of selected ingress nodes...')
            self.agent.clear_all_memory(nodes=self.ingress_nodes)
            
        if self.test_type == 'classification':
            # Start an Labels Tracker for each node
            print('Initialize labels set...')
            self.labels_set = {}
            for node in self.ingress_nodes:
                self.labels_set[node] = set()
            print(self.labels_set)
            print('Created labels set...')             
        elif self.test_type == 'emotives_value' or self.test_type == 'emotives_polarity':
            # Start an Emotives Tracker for each node
            print('Initialize emotives set...')
            self.emotives_set = {}
            for node in self.ingress_nodes:
                self.emotives_set[node] = set()
            print(self.emotives_set)
            print('Created emotives set...')
        else:
            raise Exception(
                """
                Please choose one of the test type:
                  - classification
                  - emotives_value
                  - emotives_polarity
                  
                ex.
                --> pvt.test_type='emotives_value'
                
                then, retry
                
                --> pvt.conduct_pvt()
                """
            )
        # Train Agent
        if self.turn_prediction_off_during_training == True:
            self.agent.stop_predicting(nodes=self.query_nodes)
        else:
            self.agent.start_predicting(nodes=self.query_nodes)
        print('Preparing to train agent...') 
        # for i, file_path in enumerate(log_progress(dataset.train_sequences)):
        for j, file_path in enumerate(self.dataset.train_sequences):
            if j % 100 == 0:
                print(f"train - {j}")
            with open(self.dataset.train_sequences[j], "r") as sequence_file:
                sequence = sequence_file.readlines()
                sequence = [json.loads(d) for d in sequence]
                for event in sequence:
                    self.agent.observe(data=event,nodes=self.ingress_nodes)
                    if self.test_type == 'emotives_value' or self.test_type == 'emotives_polarity':
                        for node in self.ingress_nodes:
                            self.emotives_set[node] = self.emotives_set[node].union(self.agent.get_percept_data()[node]['emotives'].keys())
                if self.test_type == 'classification':
                    for node in self.ingress_nodes:
                        self.labels_set[node] = self.labels_set[node].union(sequence[-1]['strings'])                    
                self.agent.learn(nodes=self.ingress_nodes)
        print('Finished training agent!')

    
    def test_agent(self):
        """
        Takes a testing set of gdf files, then tries to predict what it observes,
        stores the predictions for later analysis/metrics
        """
        # Initialize Testing
        # making sure agent data structure to include a single node name for general traversing of structures          
        self.agent.start_predicting(nodes=self.query_nodes)
        self.predictions = []
        self.actuals     = []
        # for i, file_path in enumerate(log_progress(dataset.test_sequences)):
        for k, file_path in enumerate(self.dataset.test_sequences):
            if k % 100 == 0:
                print(f"test - {k}")
            with open(self.dataset.test_sequences[k], "r") as sequence_file:
                self.agent.clear_wm(nodes=self.ingress_nodes)
                sequence = sequence_file.readlines()
                sequence = [json.loads(d) for d in sequence]
                if self.test_type == 'classification':
                    # observe up to last event, which has the answer    
                    for event in sequence[:-1]:
                        self.agent.observe(data=event,nodes=self.ingress_nodes)
                    # get and store predictions after observing events
                    self.predictions.append(self.agent.get_predictions(nodes=self.query_nodes))
                    # store answers in a separate list for evaluation
                    self.actuals.append(sequence[-1]['strings'])
                    for node in self.ingress_nodes:
                        self.labels_set[node] = self.labels_set[node].union(sequence[-1]['strings'])
                    # observe answer
                    self.agent.observe(sequence[-1])
                elif self.test_type == 'emotives_value' or self.test_type == 'emotives_polarity':
                    for event in sequence:
                        self.agent.observe(data=event,nodes=self.ingress_nodes)
                        for node in self.ingress_nodes:
                            self.emotives_set[node] = self.emotives_set[node].union(self.agent.get_percept_data()[node]['emotives'].keys())
                    # get and store predictions after observing events
                    self.predictions.append(self.agent.get_predictions(nodes=self.query_nodes))
                    # store answers in a separate list for evaluation
                    self.actuals.append(self.sum_sequence_emotives(sequence)) # DONE: ask if this is inside sdk already --> it isn't
                else:
                    raise Exception('Not a valid test type. Please give correct test type in order to extract the appropriate information from the dataset.')

                # learn answer (optional continous learning)
                if self.test_prediction_strategy == "continuous":
                    self.agent.learn(nodes=self.ingress_nodes)
                elif self.test_prediction_strategy == "noncontinuous":
                    continue
                else:
                    raise Exception(
                        """
                        Not a valid test prediction strategy. Please choose either 'continuous',
                        which means to learn the test sequence/answer after the agent has tried to make a prediction on that test sequence,
                        or, 'noncontinuous', which means to not learn the test sequence.
                        """
                    )
                
    
    def sum_sequence_emotives(self, sequence):
        """
        Sums all emotive values
        """
        emotives_seq = [event['emotives'] for event in sequence if event['emotives']]
        return dict(functools.reduce(operator.add, map(collections.Counter, emotives_seq)))

    
    def get_classification_metrics(self):
        """
        Builds classification data structures for each node
        """
        self.class_metrics_data_structures = {}
        for node, labels in self.labels_set.items():
            self.class_metrics_data_structures[node] = self.classification_metrics_builder(lst_of_labels=labels)
            # Let's see how well the agent scored
            overall_preds = []
            answers       = []
            for p in range(0,len(self.predictions)):
                try:
                    overall_pred = prediction_ensemble_model_classification(self.predictions[p][node])
                    if overall_pred == None:
                        # if the agent doesn't have enough information to make a prediction it wouldn't give one
                        overall_preds.append('i_dont_know')
                    else:
                        overall_preds.append(overall_pred)
                except Exception as e:
                    print('Something is wrong with the prediction')
                answers.append(self.actuals[p][0])
            try:
                accuracy = round(accuracy_score(answers,overall_preds),2)*100
            except ZeroDivisionError:
                accuracy = 0.0                 
            prec_predictions       = [p for p, a in zip(overall_preds, answers) if p != 'i_dont_know']
            prec_answers           = [a for p, a in zip(overall_preds, answers) if p != 'i_dont_know']
            try:
                precision = round(accuracy_score(prec_answers,prec_predictions),2)*100
            except ZeroDivisionError:
                precision = 0.0
            total_amount_of_questions            = len(answers)
            updated_pred_length                  = len([p for p in overall_preds if p != 'i_dont_know'])
            try:
                resp_pc = np.round(updated_pred_length/total_amount_of_questions, 2)*100
            except ZeroDivisionError:
                resp_pc = 0.0
            self.class_metrics_data_structures[node]['predictions']          = overall_preds
            self.class_metrics_data_structures[node]['actuals']              = answers
            self.class_metrics_data_structures[node]['metrics']['resp_pc']   = resp_pc
            self.class_metrics_data_structures[node]['metrics']['accuracy']  = accuracy
            self.class_metrics_data_structures[node]['metrics']['precision'] = precision
            
    
    def get_emotives_value_metrics(self):
        """
        Builds emotives value data structures for each node
        """                         
        # Build an emotives Metric Data Structure
        self.emotives_metrics_data_structures = {}
        for node, emotive_set in self.emotives_set.items():        
            self.emotives_metrics_data_structures[node] = self.emotives_value_metrics_builder(lst_of_emotives=list(emotive_set))
        # Populate Emotives Metrics
        for i, (prediction_ensemble, actual) in enumerate(zip(self.predictions, self.actuals)):
            for node_name, node_pred_ensemble in prediction_ensemble.items():
                if node_pred_ensemble:
                    modeled_emotives = self.make_modeled_emotives_(ensemble=node_pred_ensemble) # get overall prediction from a single node                    
                    for emotive_name_from_model, pred_value in modeled_emotives.items():
                        if emotive_name_from_model in list(self.emotives_metrics_data_structures[node_name].keys()):
                            self.emotives_metrics_data_structures[node_name][emotive_name_from_model]['predictions'].append(pred_value)
                            self.emotives_metrics_data_structures[node_name][emotive_name_from_model]['actuals'].append(actual[emotive_name_from_model])                           
                    left_overs = set(self.emotives_metrics_data_structures) - set(list(modeled_emotives.keys()))
                    if left_overs:
                        for emotive_name, metric_data in self.emotives_metrics_data_structures[node_name].items():
                            if emotive_name in left_overs:
                                self.emotives_metrics_data_structures[node_name][emotive_name]['predictions'].append(np.nan)
                                self.emotives_metrics_data_structures[node_name][emotive_name]['actuals'].append(actual[emotive_name])
                else:
                    for emotive_name, metric_data in self.emotives_metrics_data_structures[node_name].items():
                        self.emotives_metrics_data_structures[node_name][emotive_name]['predictions'].append(np.nan)
                        self.emotives_metrics_data_structures[node_name][emotive_name]['actuals'].append(actual[emotive_name])
                # Create Metrics
                for node_name, node_emotive_metrics in self.emotives_metrics_data_structures.items():
                    # calculate response rate percentage
                    for emotive_name, data in node_emotive_metrics.items():
                        total_amount_of_questions            = len(data['actuals'])
                        updated_pred_length                  = len([p for p in data['predictions'] if p is not np.nan])
                        try:
                            resp_pc = np.round(updated_pred_length/total_amount_of_questions, 2)*100
                        except ZeroDivisionError:
                            resp_pc = 0.0
                        self.emotives_metrics_data_structures[node_name][emotive_name]['metrics']['resp_pc'] = resp_pc                            
                    # calculate rmse
                    for emotive_name, data in node_emotive_metrics.items():
                        error_lst = [p-a for p, a in zip(data['predictions'], data['actuals']) if p is not np.nan]
                        if error_lst:
                            rmse = np.square(error_lst).mean()
                            self.emotives_metrics_data_structures[node_name][emotive_name]['metrics']['rmse'] = rmse
                    # calculate smape_precision
                    for emotive_name, data in node_emotive_metrics.items():
                        smape_prec_predictions       = [p for p, a in zip(data['predictions'], data['actuals']) if p is not np.nan]
                        smape_prec_actuals           = [a for p, a in zip(data['predictions'], data['actuals']) if p is not np.nan]
                        smape_prec_predictions_array = np.array(smape_prec_predictions)
                        smape_prec_actuals_array     = np.array(smape_prec_actuals)
                        try:
                            smape_prec = np.round(1.0-(1.0/len(smape_prec_actuals_array)*np.nansum(np.abs(smape_prec_actuals_array - smape_prec_predictions_array)/(np.abs(smape_prec_actuals_array)+np.abs(smape_prec_predictions_array))) ),2)*100
                        except ZeroDivisionError:
                            smape_prec = None
                        self.emotives_metrics_data_structures[node_name][emotive_name]['metrics']['smape_prec'] = smape_prec        

                
    def get_emotives_polarity_metrics(self):
        """
        Builds emotives polarity data structures for each node
        """
        # Build an emotives Metric Data Structure
        self.emotives_metrics_data_structures = {}
        for node, emotive_set in self.emotives_set.items():        
            self.emotives_metrics_data_structures[node] = self.emotives_polarity_metrics_builder(lst_of_emotives=list(emotive_set))
        # Populate Emotives Metrics
        for i, (prediction_ensemble, actual) in enumerate(zip(self.predictions, self.actuals)):
            for node_name, node_pred_ensemble in prediction_ensemble.items():
                if node_pred_ensemble:
                    modeled_emotives = self.make_modeled_emotives_(ensemble=node_pred_ensemble) # get overall prediction from a single node
                    for emotive_name_from_model, pred_value in modeled_emotives.items():
                        if emotive_name_from_model in list(self.emotives_metrics_data_structures[node_name].keys()):
                            self.emotives_metrics_data_structures[node_name][emotive_name_from_model]['predictions'].append(pred_value)
                            self.emotives_metrics_data_structures[node_name][emotive_name_from_model]['actuals'].append(actual[emotive_name_from_model])                           
                    left_overs = set(self.emotives_metrics_data_structures) - set(list(modeled_emotives.keys()))
                    if left_overs:
                        for emotive_name, metric_data in self.emotives_metrics_data_structures[node_name].items():
                            if emotive_name in left_overs:
                                self.emotives_metrics_data_structures[node_name][emotive_name]['predictions'].append(np.nan)
                                self.emotives_metrics_data_structures[node_name][emotive_name]['actuals'].append(actual[emotive_name])
                else:
                    for emotive_name, metric_data in self.emotives_metrics_data_structures[node_name].items():
                        self.emotives_metrics_data_structures[node_name][emotive_name]['predictions'].append(np.nan)
                        self.emotives_metrics_data_structures[node_name][emotive_name]['actuals'].append(actual[emotive_name])
                # Create Metrics        
                for node_name, node_emotive_metrics in self.emotives_metrics_data_structures.items():
                    # calculate response rate percentage
                    for emotive_name, data in node_emotive_metrics.items():
                        total_amount_of_questions            = len(data['actuals'])
                        updated_pred_length                  = len([p for p in data['predictions'] if p is not np.nan])
                        try:
                            resp_pc = np.round(updated_pred_length/total_amount_of_questions, 2)*100
                        except ZeroDivisionError:
                            resp_pc = 0.0
                        self.emotives_metrics_data_structures[node_name][emotive_name]['metrics']['resp_pc'] = resp_pc
                    # calculate accuracy                    
                    for emotive_name, data in node_emotive_metrics.items():
                        polarity_accuracy_loading_dock  = []
                        polarity_precision_loading_dock = []
                        for p, a in zip(data['predictions'], data['actuals']): 
                            if p is np.nan:
                                polarity_accuracy_loading_dock.append("incorrect")
                            elif p is not np.nan:
                                if p*a > 0:
                                    polarity_accuracy_loading_dock.append("correct")
                                elif p*a < 0:
                                    polarity_accuracy_loading_dock.append("incorrect")
                            else:
                                raise Exception("Something is wrong with the data type...") 
                        try:        
                            accuracy = round(polarity_accuracy_loading_dock.count("correct")/len(polarity_accuracy_loading_dock), 2)*100
                        except Exception as e:
                            accuracy = 0.0                                
                        # populate accuracy to data structure
                        self.emotives_metrics_data_structures[node_name][emotive_name]['metrics']['accuracy']  = accuracy
                        # calculate precision
                        for p, a in zip(data['predictions'], data['actuals']): 
                            if p is np.nan:
                                continue
                            elif p is not np.nan:
                                if p*a > 0:
                                    polarity_precision_loading_dock.append("correct")
                                elif p*a < 0:
                                    polarity_precision_loading_dock.append("incorrect")
                            else:
                                raise Exception("Something is wrong with the data type...")
                        try:
                            precision = round(polarity_precision_loading_dock.count("correct")/len(polarity_precision_loading_dock), 2)*100
                        except Exception as e:
                            precision = 0.0
                        # populate precision to data structure
                        self.emotives_metrics_data_structures[node_name][emotive_name]['metrics']['precision'] = precision

    
    def plot_confusion_matrix(self, test_num):
        """
        Takes a node classification test to create a confusion matrix. This version includes the i_dont_know or unknown label.
        """
        
        for node_name, class_metrics_data in self.class_metrics_data_structures.items():
            print(f'-----------------Test#{test_num}-{node_name}-Plots-----------------')
            cm           = confusion_matrix(class_metrics_data['actuals'], class_metrics_data['predictions'], labels=class_metrics_data['labels'])
            disp         = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=class_metrics_data['labels'])
            disp.plot()
            plt.show()
    
    
    def plot_emotives_value_charts(self, test_num):
        
        for node_name, node_emotive_metrics in self.emotives_metrics_data_structures.items():
            print(f'-----------------Test#{test_num}-{node_name}-Plots-----------------')
            for emotive_name, data in sorted(node_emotive_metrics.items()):
                labels = 'precision', 'miss'
                if data['metrics']['smape_prec'] == None:
                    sizes = [0, 100]
                else:
                    sizes = [data['metrics']['smape_prec'], 100 - data['metrics']['smape_prec']]
                explode = (0, 0)
                fig1, ax1 = plt.subplots()
                ax1.title.set_text(f'{node_name} - {emotive_name}')
                ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                colors = ['gray', 'skyblue']
                patches, texts = plt.pie(sizes, colors=colors, startangle=90)
                plt.legend(patches, labels, loc="best")
                plt.figtext(0, 0, f"{pd.Series(data['metrics']).round(1).to_string()}", ha="center", fontsize=18, bbox={"facecolor":"orange", "alpha":0.5, "pad":5})
                try:
                    plt.savefig(f"{self.results_filepath}/{test_num}_{node_name}_{emotive_name}.png", dpi=300, bbox_inches='tight')
                except Exception as e:
                    print("Not able to save figure in assigned results directory! Please add an appropriate directory.")
                    pass
                plt.show()
                print('---------------------')


    def emotives_value_metrics_builder(self, lst_of_emotives):
        """
        Create Metrics Data Structure for each emotive in testset
        """
        emotives_metrics_data_structure = {}
        for emotive in lst_of_emotives:
            emotives_metrics_data_structure[emotive] = {
                "predictions": [],
                "actuals": [],
                "metrics": {
                    "resp_pc": None, # response rate percentage
                    "rmse": None,
        #             "smape_acc": None, # NOTE: Took this out because the metrics for values cannot handle unknown predictions, so only precision matters
                    "smape_prec": None
                }
            }
        return emotives_metrics_data_structure
    
    
    def emotives_polarity_metrics_builder(self, lst_of_emotives):
        """
        Create Metrics Data Structure for each emotive in testset
        """
        emotives_metrics_data_structure = {}
        for emotive in lst_of_emotives:
            emotives_metrics_data_structure[emotive] = {
                "predictions": [],
                "actuals": [],
                "metrics": {
                    "resp_pc": None,
                    "accuracy": None,
                    "precision": None
                }
            }
        return emotives_metrics_data_structure
    
    
    def classification_metrics_builder(self, lst_of_labels):
        """
        Create Metrics Data Structure for a classification problem where labels are tracked and used.
        """
        classification_metrics_data_structure = {
            'predictions': [],
            'actuals': [],
            'labels': list(lst_of_labels) + ['i_dont_know'],
            'metrics': {
                'resp_pc': None,
                'accuracy': None,
                'precision': None
            }
        }
        return classification_metrics_data_structure

    
    def model_per_emotive_(self, ensemble, emotive, potential_normalization_factor):
        "Using a Weighted Moving Average, though the 'moving' part refers to the prediction index."
        ## using a weighted posterior_probability = potential/marginal_probability
        ## FORMULA: pv + ( (Uprediction_2-pv)*(Wprediction_2) + (Uprediction_3-pv)*(Wprediction_3)... )/mp
        # A Weighted Moving Average puts more weight on recent data and less on past data. This is done by multiplying each bar’s price by a weighting factor. Because of its unique calculation, WMA will follow prices more closely than a corresponding Simple Moving Average.
        # https://www.fidelity.com/learning-center/trading-investing/technical-analysis/technical-indicator-guide/wma#:~:text=Description,a%20corresponding%20Simple%20Moving%20Average.
        _found = False
        while not _found:
            for i in range(0,len(ensemble)):
                if emotive in ensemble[i]['emotives'].keys():
                    _found = True
                    principal_value = ensemble[i]['emotives'][emotive]  ## Let's use the "best" match (i.e. first showing of this emotive) as our starting point. Alternatively, we can use,say, the average of all values before adjusting.
                    break
            if i == len(ensemble) and not _found:
                return 0
            if i == len(ensemble) and _found:
                return principal_value
        marginal_probability = sum([x["potential"] for x in ensemble]) # NOTE: marginal_probability = mp, this might the wrong calculation for this variable.
        weighted_moving_value = 0 # initialized top portion of summation
        for x in ensemble[i+1:]:
            if emotive in x['emotives']:
                weighted_moving_value += (x['emotives'][emotive] - (principal_value)) * ((x["potential"] / potential_normalization_factor))
        weighted_moving_emotive_average = principal_value + (weighted_moving_value / marginal_probability)
        return weighted_moving_emotive_average


    def make_modeled_emotives_(self, ensemble):
        '''The emotives in the ensemble are of type: 'emotives':[{'e1': 4, 'e2': 5}, {'e2': 6}, {'e1': 5 'e3': -4}]'''
        emotives_set = set()
        potential_normalization_factor = sum([p['potential'] for p in ensemble])

        filtered_ensemble = []
        for p in ensemble:
            new_record = p
            new_record['emotives'] = average_emotives([p['emotives']]) # AVERAGE
            filtered_ensemble.append(new_record)

    #     filtered_ensemble = bucket_predictions(filtered_ensemble) # BUCKET

    #     pprint.pprint(f"filtered_ensemble = {filtered_ensemble}")
        for p in filtered_ensemble:
            emotives_set = emotives_set.union(p['emotives'].keys())
        return {emotive: self.model_per_emotive_(ensemble, emotive, potential_normalization_factor) for emotive in emotives_set}
    
    
    def update_test_results_w_hive_classification_metrics(self, pvt_test_result):
        """
        Update pvt test result metrics with hive classifications metrics
        """
        # add hive_metrics
        hive_metrics = {
            'predictions': [],
            'actuals': [],
            'labels': [],
            'metrics': {
                'resp_pc': None,
                'accuracy': None,
                'precision': None
            }
        }

        # get hive labels set
        hive_label_count = []
        for node_name, test_data in pvt_test_result.items():
            if node_name != 'hive':
                for label in test_data['labels']:
                    hive_label_count.append(label)

        hive_label_set_lst = list(set(hive_label_count))
        
        # add hive metrics dictionary to pvt results
        pvt_test_result['hive'] = hive_metrics
        
        pvt_test_result['hive']['labels'] = hive_label_set_lst


        # get predictions to get hive classification of all nodes
        for i in range(0, len(self.predictions)):
            pvt_test_result['hive']['predictions'].append(hive_model_classification(ensembles=self.predictions[i]))

        # get actuals of test   
        for i in range(0, len(self.actuals)):
            pvt_test_result['hive']['actuals'].append(self.actuals[i][0])

        # get hive accuracy of test
        for node_name, test_data in pvt_test_result.items(): 
            if node_name == 'hive':
                try:
                    hive_accuracy = round(accuracy_score(test_data['actuals'],test_data['predictions']),2)*100
                except ZeroDivisionError:
                    hive_accuracy = 0.0
        pvt_test_result['hive']['metrics']['accuracy'] = hive_accuracy

        # get hive precision of test            
        for node_name, test_data in pvt_test_result.items(): 
            if node_name == 'hive':
                prec_predictions       = [p for p, a in zip(test_data['predictions'], test_data['actuals']) if p != 'i_dont_know']
                prec_answers           = [a for p, a in zip(test_data['predictions'], test_data['actuals']) if p != 'i_dont_know']
                try:
                    hive_precision = round(accuracy_score(prec_answers,prec_predictions),2)*100
                except ZeroDivisionError:
                    hive_precision = 0.0
        pvt_test_result['hive']['metrics']['precision'] = hive_precision

        # get hive response rate percentage of test
        for node_name, test_data in pvt_test_result.items(): 
            if node_name == 'hive':
                total_amount_of_questions            = len(test_data['actuals'])
                updated_pred_length                  = len([p for p in test_data['predictions'] if p != 'i_dont_know'])
                try:
                    hive_resp_pc = np.round(updated_pred_length/total_amount_of_questions, 2)*100
                except ZeroDivisionError:
                    hive_resp_pc = 0.0
        pvt_test_result['hive']['metrics']['resp_pc'] = hive_resp_pc

#         self.pvt_test_result 
        pprint.pprint(pvt_test_result)
        return pvt_test_result
    
    
    def update_test_results_w_hive_emotives_value_metrics(self, pvt_test_result):
        """
        Update pvt test result metrics with hive classifications metrics
        """
        all_nodes_emotives_set = set()
        for node, emotives in pvt.emotives_set.items():
            for emotive in emotives:
                all_nodes_emotives_set.add(emotive)   
        hive_emotives_value_metrics_lst = []
        for emotive in all_nodes_emotives_set:
            hive_emotives_value_metrics_template = {
                f'{emotive}': {
                    'resp_pc': [],
                    'rmse': [],
                    'smape_prec': []
                }
            }
            hive_emotives_value_metrics_lst.append(hive_emotives_value_metrics_template)    
        for test_num, test_metric in pvt.pvt_results.items():
            for node, test_data in test_metric.items():
                for emotive, emotive_metric in test_data.items():
                    if emotive_metric['metrics']['resp_pc'] != 0.0 and emotive in all_nodes_emotives_set:
                        for hive_emotive_metric_dict in hive_emotives_value_metrics_lst:
                            if emotive in hive_emotive_metric_dict.keys():
                                hive_emotive_metric_dict[emotive]['resp_pc'].append(emotive_metric['metrics']['resp_pc'])
                                hive_emotive_metric_dict[emotive]['rmse'].append(emotive_metric['metrics']['rmse'])
                                hive_emotive_metric_dict[emotive]['smape_prec'].append(emotive_metric['metrics']['smape_prec'])
        for emotive_metrics in hive_emotives_value_metrics_lst:
            for emotive_name, metric_data in emotive_metrics.items():
                for metric_name, metric_data_lst in metric_data.items():
                    emotive_metrics[emotive_name][metric_name] = sum(emotive_metrics[emotive_name][metric_name])/len(emotive_metrics[emotive_name][metric_name])
        pvt_test_result['hive'] = hive_emotives_value_metrics_lst
        pprint.pprint(pvt_test_result)
        return pvt_test_result
    
    
    def update_test_results_w_hive_emotives_polarity_metrics(self, pvt_test_result):
        """
        Update pvt test result metrics with hive classifications metrics
        """
        all_nodes_emotives_set = set()
        for node, emotives in pvt.emotives_set.items():
            for emotive in emotives:
                all_nodes_emotives_set.add(emotive)   
        hive_emotives_value_metrics_lst = []
        for emotive in all_nodes_emotives_set:
            hive_emotives_value_metrics_template = {
                f'{emotive}': {
                    'resp_pc': [],
                    'accuracy': [],
                    'precision': []
                }
            }
            hive_emotives_value_metrics_lst.append(hive_emotives_value_metrics_template)    
        for test_num, test_metric in pvt.pvt_results.items():
            for node, test_data in test_metric.items():
                for emotive, emotive_metric in test_data.items():
                    if emotive_metric['metrics']['resp_pc'] != 0.0 and emotive in all_nodes_emotives_set:
                        for hive_emotive_metric_dict in hive_emotives_value_metrics_lst:
                            if emotive in hive_emotive_metric_dict.keys():
                                hive_emotive_metric_dict[emotive]['resp_pc'].append(emotive_metric['metrics']['resp_pc'])
                                hive_emotive_metric_dict[emotive]['accuracy'].append(emotive_metric['metrics']['accuracy'])
                                hive_emotive_metric_dict[emotive]['precision'].append(emotive_metric['metrics']['precision'])
        for emotive_metrics in hive_emotives_value_metrics_lst:
            for emotive_name, metric_data in emotive_metrics.items():
                for metric_name, metric_data_lst in metric_data.items():
                    emotive_metrics[emotive_name][metric_name] = sum(emotive_metrics[emotive_name][metric_name])/len(emotive_metrics[emotive_name][metric_name])
        pvt_test_result['hive'] = hive_emotives_value_metrics_lst
        pprint.pprint(pvt_test_result)
        return pvt_test_result