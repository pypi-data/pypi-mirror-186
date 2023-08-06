import collections
import functools
import json
import operator
from copy import deepcopy
from uuid import uuid4
# Data
from sklearn.metrics import accuracy_score
import numpy as np

# Gaius Agent
from ia.gaius.agent_client import AgentClient
from ia.gaius.prediction_models import *
from ia.gaius.data_ops import Data, MongoData, MongoResults
from ia.gaius.tests.pvt_utils import *

class PVTMessage():
    """Wrapper for PVT socket messages to be sent during training and testing"""
    def __init__(self, status: str, current_record: int, total_record_count: int, 
                 metrics: dict, cur_test_num: int, total_test_num: int, test_id: str=None, user_id: str=''):
        self.status = status
        self.current_record = current_record
        self.total_record_count = total_record_count
        self.metrics = metrics
        self.test_id = test_id
        self.user_id = user_id
        self.cur_test_num = cur_test_num
        self.total_test_num = total_test_num
        
    
    def toJSON(self):
        return {'status': self.status,
                'current_record': self.current_record,
                'total_record_count': self.total_record_count,
                'metrics': self.metrics,
                'test_id': self.test_id,
                'user_id': self.user_id,
                'cur_test_num': self.cur_test_num,
                'total_test_num': self.total_test_num
                }

class PerformanceValidationTest():
    """
    Performance Validation Test (PVT) - Splits a GDF folder into training and testing sets.
    Based on the test type certain visualizations will be produced.
    
    Test types:
    
    - Classification
    - Emotive Value
    - Emotives Polarity
    """
    def __init__(self, agent: AgentClient,ingress_nodes: list,query_nodes: list,num_of_tests: int, pct_of_ds: float,
                 pct_res_4_train:float, test_type:str, dataset_location:str='filepath', results_filepath=None, ds_filepath:str=None, test_prediction_strategy="continuous",
                 clear_all_memory_before_training:bool=True, turn_prediction_off_during_training:bool=False, 
                 shuffle:bool=False, sio=None, task=None, user_id:str=None, mongo_db=None, dataset_info:dict=None, test_id=None):
        """Initialize the PVT object with all required parameters for execution

        Args:
            agent (AgentClient): GAIuS Agent to use for trainings
            ingress_nodes (list): Ingress nodes for the GAIuS Agent (see :func:`ia.gaius.agent_client.AgentClient.set_query_nodes`)
            query_nodes (list): Query nodes for the GAIuS Agent (see :func:`ia.gaius.agent_client.AgentClient.set_query_nodes`)
            num_of_tests (int): Number of test iterations to complete
            pct_of_ds (float): Percent of the dataset to use for PVT (overall)
            pct_res_4_train (float): Percent of the dataset to be reserved for training
            test_type (str): classification, emotives_value, or emotives_polarity
            dataset_location (str): Location of dataset to utilise, "mongodb", or "filepath"            
            results_filepath (_type_): Where to store PVT results
            ds_filepath (str): Path to the directory containing training GDFs
            test_prediction_strategy (str, optional): _description_. Defaults to "continuous".
            clear_all_memory_before_training (bool, optional): Whether the GAIuS agent's memory should be cleared before each training. Defaults to True.
            turn_prediction_off_during_training (bool, optional): Whether predictions should be disabled during training to reduce computational load. Defaults to False.
            shuffle (bool, optional): Whether dataset should be shuffled before each test iteration. Defaults to False.
            sio (_type_, optional): SocketIO object to emit information on. Defaults to None.
            task (_type_, optional): Celery details to emit information about. Defaults to None.
            user_id (str, optional): user_id to emit information to on SocketIO. Defaults to ''.
            mongo_db (pymongo.MongoClient, optional): MongoDB where dataset should be retrieved from
            dataset_info (dict, optional): information about how to retrieve dataset, used for MongoDB query. If dataset_location is mongodb, this must have the user_id, dataset_id, results_collection, logs_collection, and data_files_collection_name keys
            test_id (str, optional): unique identifier to be sent with messages about this test. Also used for storing to mongodb
        """
        
        self.agent                               = agent
        self.ingress_nodes                       = ingress_nodes
        self.query_nodes                         = query_nodes
        self.num_of_tests                        = num_of_tests
        self.dataset_location                    = dataset_location
        self.ds_filepath                         = ds_filepath
        self.results_filepath                    = results_filepath
        self.pct_of_ds                           = pct_of_ds
        self.pct_res_4_train                     = pct_res_4_train
        self.shuffle                             = shuffle
        self.test_type                           = test_type
        self.clear_all_memory_before_training    = clear_all_memory_before_training
        self.turn_prediction_off_during_training = turn_prediction_off_during_training
        self.test_prediction_strategy            = test_prediction_strategy
        
        self.emotives_set                        = None
        self.labels_set                          = None
        self.predictions                         = None
        self.actuals                             = None
        self.emotives_metrics_data_structures    = None
        self.class_metrics_data_structures       = None
        self.metrics_dataframe                   = None
        self.pvt_results                         = None
        self.sio                                 = sio
        self.task                                = task
        self.user_id                             = user_id
        self.mongo_db                            = mongo_db
        self.dataset_info                        = dataset_info
        self.test_id                             = test_id
        self.testing_log                         = []
        self.mongo_results                       = None
        
        
        if self.user_id == '':
            self.user_id = uuid4().hex
        # if self.test_id == None:
        #     self.test_id == uuid4().hex
            
        if dataset_location == 'mongodb':
            self.dataset = MongoData(mongo_dataset_details=self.dataset_info, data_files_collection_name=self.dataset_info['data_files_collection_name'], mongo_db=mongo_db)
            self.mongo_results = MongoResults(mongo_db=self.mongo_db, result_collection_name=self.dataset_info['results_collection'], 
                                              log_collection_name=self.dataset_info['logs_collection'], test_id=self.test_id, user_id=self.user_id,
                                              dataset_id=self.dataset_info['dataset_id'])
        elif dataset_location == 'filepath':
            self.dataset = Data(data_directories=[self.ds_filepath]) 
        else:
            raise Exception(f'unknown value for dataset location: {dataset_location}')
            
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

    
    def run_classification_pvt(self):
        self.pvt_results = {}  
        self.test_num = 0
        self.testing_log = []
        for test_num in range(0,self.num_of_tests):
            self.test_num = test_num
            print(f'Conducting Test # {test_num}')
            print('\n---------------------\n')
            
            self.prepare_datasets()
            
            if self.sio:
                self.sio.emit('pvt_status', 
                              PVTMessage(status='training', current_record=0, total_record_count=len(self.dataset.train_sequences), 
                                       metrics={}, cur_test_num=self.test_num, total_test_num=self.num_of_tests, 
                                       test_id=self.test_id, user_id=self.user_id).toJSON(), to=self.user_id)
            self.train_agent()
            
            self.testing_log.append([])

            self.test_agent()
            
            for k, labels in self.labels_set.items():
                self.labels_set[k] = set([label.rsplit('|', maxsplit=1)[-1] for label in labels])
            print('Getting Classification Metrics...')
            self.get_classification_metrics()
            print('Saving results to pvt_results...')
            self.pvt_results[f'test_num_{test_num}_metrics'] = self.class_metrics_data_structures
            self.pvt_results[f'test_num_{test_num}_metrics'] = self.update_test_results_w_hive_classification_metrics(self.pvt_results[f'test_num_{test_num}_metrics'])

            try:
                print('Plotting Results...')
                plot_confusion_matrix(test_num=test_num, class_metrics_data_structures=self.class_metrics_data_structures)
            except Exception as e:
                print(f'error plotting results from classification pvt: {e}')
                pass
                
            if self.sio:
                self.sio.emit('pvt_status', 
                              PVTMessage(status='finished', current_record=0, total_record_count=0, 
                                       metrics=self.pvt_results, cur_test_num=self.num_of_tests, total_test_num=self.num_of_tests, 
                                       test_id=self.test_id, user_id=self.user_id).toJSON(), to=self.user_id)

            if self.mongo_results:
                self.mongo_results.saveResults(self.pvt_results)
            
        return
    
    def run_emotive_value_pvt(self):
        self.pvt_results = {}
        for test_num in range(0,self.num_of_tests):
            
            print(f'Conducting Test # {test_num}')
            print('\n---------------------\n')
            
            self.prepare_datasets()

            self.train_agent()

            self.test_agent()

            print('Getting Emotives Value Metrics...')
            self.get_emotives_value_metrics()
            print('Saving results to pvt_results...')
            self.pvt_results[f'test_num_{test_num}_metrics'] = self.emotives_metrics_data_structures
            self.pvt_results[f'test_num_{test_num}_metrics'] = self.update_test_results_w_hive_emotives_value_metrics(self.pvt_results[f'test_num_{test_num}_metrics'])

            print('Plotting Results...')
            self.plot_emotives_value_charts(test_num=test_num)
        return
    
    def run_emotive_polarity_pvt(self):
        self.pvt_results = {}
        for test_num in range(0,self.num_of_tests):
            
            print(f'Conducting Test # {test_num}')
            print('\n---------------------\n')
            self.prepare_datasets()
            
            print("Training Agent...")
            self.train_agent()
            
            print("Testing Agent...")
            self.test_agent()

            print('Getting Emotives Polarity Metrics...')
            self.get_emotives_polarity_metrics()
            print('Saving results to pvt_results...')
            self.pvt_results[f'test_num_{test_num}_metrics'] = self.emotives_metrics_data_structures
            self.pvt_results[f'test_num_{test_num}_metrics'] = self.update_test_results_w_hive_emotives_polarity_metrics(self.pvt_results[f'test_num_{test_num}_metrics'])
        return
    
    def conduct_pvt(self):
        """
        Function called to execute the PVT session. Determines test to run based on 'test_type' attribute
        
        Results from PVT is stored in the 'pvt_results' attribute
        
        .. note:: 

            A complete example is shown in the :func:`__init__` function above. Please see that documentation for further information about how to conduct a PVT test
        
        """
        try:
            # Validate Test Type    
            if self.test_type == 'classification':
                print("Conducting Classification PVT...\n")
                self.run_classification_pvt()
            

            elif self.test_type == 'emotives_value':
                print("Conducting Emotives Value PVT...\n")
                self.run_emotive_value_pvt()
            

            elif self.test_type == 'emotives_polarity':
                print("Conducting Emotives Polarity PVT...\n")
                self.run_emotive_polarity_pvt()

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
        except Exception as e:
            print(f'failed to conduct PVT test, test_type={self.test_type}: {e}')
            raise e

         
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
        
        train_seq_len = len(self.dataset.train_sequences)
        for j, _ in enumerate(self.dataset.train_sequences):
            
            training_msg = PVTMessage(status='training', current_record=j, total_record_count=train_seq_len, 
                                       metrics={}, cur_test_num=self.test_num+1, total_test_num=self.num_of_tests, 
                                       test_id=self.test_id, user_id=self.user_id)
            if self.sio:
                self.sio.emit('pvt_status', training_msg.toJSON(), to=self.user_id)
            # insert into test_log in mongo, if using mongodb
            if self.mongo_results:
                    self.mongo_results.addLogRecord(type='training', record=training_msg.toJSON())
            
            if j % 10 == 0:
                if self.task:
                    if self.task.is_aborted():
                        print(f'about to abort {self.task.id =}, {self.test_id=}')
                        if self.sio:
                            print(f'Sending abort message')
                            abort_msg = PVTMessage(status='aborted', current_record=j, total_record_count=train_seq_len, 
                                       metrics={}, cur_test_num=self.test_num+1, total_test_num=self.num_of_tests, 
                                       test_id=self.test_id, user_id=self.user_id)
                            self.sio.emit('pvt_status', abort_msg.toJSON(), to=self.user_id)
                        if self.mongo_results:
                            print(f'cleaning up MongoDB')
                            self.mongo_results.deleteResults()
                            
                        return
                    
            
            if j % 100 == 0:
                print(f"train - {j}")
            if self.dataset_location == 'filepath':
                with open(self.dataset.train_sequences[j], "r") as sequence_file:
                    sequence = sequence_file.readlines()
                    sequence = [json.loads(d) for d in sequence]
            elif self.dataset_location == 'mongodb':
                sequence = self.dataset.getSequence(self.dataset.train_sequences[j])
            else:
                raise Exception(f"dataset location {self.dataset_location} is unknown")
            
            
            for event in sequence:
                self.agent.observe(data=event,nodes=self.ingress_nodes)
                if self.test_type == 'emotives_value' or self.test_type == 'emotives_polarity':
                    for node in self.ingress_nodes:
                        self.emotives_set[node].update(self.agent.get_percept_data()[node]['emotives'].keys())
            if self.test_type == 'classification':
                for node in self.ingress_nodes:
                    self.labels_set[node].update(sequence[-1]['strings'])                    
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
        self.testing_log[self.test_num] = []
        # for i, file_path in enumerate(log_progress(dataset.test_sequences)):
        
        test_step_info = {}
        test_seq_len = len(self.dataset.test_sequences)
        for k, _ in enumerate(self.dataset.test_sequences):
            
            if k % 10 == 0:
                if self.task:
                    if self.task.is_aborted():
                        print(f'about to abort {self.task.id =}, {self.test_id=}')
                        if self.sio:
                            print(f'Sending abort message')
                            abort_msg = PVTMessage(status='aborted', current_record=k, total_record_count=test_seq_len, 
                                       metrics={}, cur_test_num=self.test_num+1, total_test_num=self.num_of_tests, 
                                       test_id=self.test_id, user_id=self.user_id)
                            self.sio.emit('pvt_status', abort_msg.toJSON(), to=self.user_id)
                        if self.mongo_results:
                            print(f'cleaning up MongoDB')
                            self.mongo_results.deleteResults()
                        return
            
            
            if k % 100 == 0:
                print(f"test - {k}")
            if self.dataset_location == 'filepath':
                with open(self.dataset.test_sequences[k], "r") as sequence_file:
                    sequence = sequence_file.readlines()
                    sequence = [json.loads(d) for d in sequence]
            elif self.dataset_location == 'mongodb':
                sequence = self.dataset.getSequence(self.dataset.test_sequences[k])
            else:
                raise Exception(f"dataset location {self.dataset_location} is unknown")
            
            self.agent.clear_wm(nodes=self.ingress_nodes)
            if self.test_type == 'classification':
                # observe up to last event, which has the answer    
                for event in sequence[:-1]:
                    self.agent.observe(data=event,nodes=self.ingress_nodes)
                # get and store predictions after observing events
                self.predictions.append(self.agent.get_predictions(nodes=self.query_nodes))
                # store answers in a separate list for evaluation
                classifications_split = [label.rsplit('|', maxsplit=1)[-1] for label in sequence[-1]['strings']]
                self.actuals.append(deepcopy(classifications_split))
                for node in self.ingress_nodes:
                    self.labels_set[node].update(sequence[-1]['strings'])

                # get predicted classification on the fly, so we can save to mongo individually
                pred_dict = {node: self.predictions[k][node] for node in self.query_nodes}
                for key in pred_dict:
                    pred_dict[key] = prediction_ensemble_model_classification(pred_dict[key])
                    if pred_dict[key] == None:
                        pred_dict[key] = 'i_dont_know'
                test_step_info.update({'idx': k, 'predicted': pred_dict, 'actual': classifications_split})
                test_step_info = self.compute_incidental_probabilities(test_step_info=test_step_info)
                # observe answer
                self.agent.observe(sequence[-1], nodes=self.ingress_nodes)
            elif self.test_type == 'emotives_value' or self.test_type == 'emotives_polarity':
                for event in sequence:
                    self.agent.observe(data=event,nodes=self.ingress_nodes)
                    for node in self.ingress_nodes:
                        self.emotives_set[node].update(self.agent.get_percept_data()[node]['emotives'].keys())
                # get and store predictions after observing events
                self.predictions.append(self.agent.get_predictions(nodes=self.query_nodes))
                # store answers in a separate list for evaluation
                self.actuals.append(self.sum_sequence_emotives(sequence)) # DONE: ask if this is inside sdk already --> it isn't

                pred_dict = {node: self.predictions[k][node] for node in self.query_nodes}
                for key in pred_dict:
                    pred_dict[key] = make_modeled_emotives_(pred_dict[key])
                
                test_step_info.update({'idx': k, 'predicted': pred_dict, 'actual': self.actuals[k]})

            else:
                raise Exception('Not a valid test type. Please give correct test type in order to extract the appropriate information from the dataset.')

            
            # prepare test step message
            test_step_msg = PVTMessage(status='testing', current_record=k, total_record_count=test_seq_len, 
                                    metrics=test_step_info, cur_test_num=self.test_num+1, total_test_num=self.num_of_tests, 
                                    test_id=self.test_id, user_id=self.user_id)
            
            # append to testing log TODO: make this in Mongo if available
            self.testing_log[self.test_num].append(test_step_msg.toJSON())
            
            # insert into test_log in mongo, if using mongodb
            if self.mongo_results:
                    self.mongo_results.addLogRecord(type='testing', record=test_step_msg.toJSON())
                    
            # emit socketIO message
            if self.sio:
                self.sio.emit('pvt_status', test_step_msg.toJSON(), to=self.user_id)

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
            self.class_metrics_data_structures[node] = classification_metrics_builder(lst_of_labels=labels)
            # Let's see how well the agent scored
            overall_preds = []
            answers       = []
            for p in range(0,len(self.predictions)):
                try:
                    # print(f'{self.predictions[p][node]=}')
                    overall_pred = prediction_ensemble_model_classification(self.predictions[p][node])
                    # print(f'{overall_pred=}')
                    if overall_pred == None:
                        # if the agent doesn't have enough information to make a prediction it wouldn't give one
                        overall_preds.append('i_dont_know')
                    else:
                        overall_preds.append(overall_pred)
                except Exception as e:
                    print('Something is wrong with the prediction')
                answers.append(self.actuals[p][0])
                # print(f'appending {self.actuals[p][0]} to answers')
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
            
    def compute_incidental_probabilities(self, test_step_info: dict):
        """Keep track of how well each node is doing during the testing phase. To be used for live visualizations
        
        Args:
            test_step_info (dict, required): Dictionary containing information about the current predicted, actual answers, and presently holds the prior running_accuracy. 
            Will update with the new running accuracy and return
            
        Returns:
            dict: updated test_step_info with the current running accuracy
        """
        idx = test_step_info['idx']
        if 'running_accuracy' not in test_step_info:
            test_step_info['running_accuracy'] = {}
            for k in test_step_info['predicted'].keys():
                if test_step_info['predicted'][k] in test_step_info['actual']:
                    test_step_info['running_accuracy'][k] = 1.0
                else:
                    test_step_info['running_accuracy'][k] = 0.0
        else:
            # print(f'{test_step_info["running_accuracy"]=}, {idx=}')
            for k in test_step_info['predicted'].keys():
                if test_step_info['predicted'][k] in test_step_info['actual']:
                    test_step_info['running_accuracy'][k] = (test_step_info['running_accuracy'][k]*(idx) + 1)/(idx+1)
                else:
                    test_step_info['running_accuracy'][k] = (test_step_info['running_accuracy'][k]*(idx))/(idx+1)
        return test_step_info
    
    def get_emotives_value_metrics(self):
        """
        Builds emotives value data structures for each node
        """                         
        # Build an emotives Metric Data Structure
        self.emotives_metrics_data_structures = {}
        for node, emotive_set in self.emotives_set.items():        
            self.emotives_metrics_data_structures[node] = emotives_value_metrics_builder(lst_of_emotives=list(emotive_set))
        # Populate Emotives Metrics
        for i, (prediction_ensemble, actual) in enumerate(zip(self.predictions, self.actuals)):
            for node_name, node_pred_ensemble in prediction_ensemble.items():
                if node_pred_ensemble:
                    modeled_emotives = make_modeled_emotives_(ensemble=node_pred_ensemble) # get overall prediction from a single node                    
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
            self.emotives_metrics_data_structures[node] = emotives_polarity_metrics_builder(lst_of_emotives=list(emotive_set))
        # Populate Emotives Metrics
        for i, (prediction_ensemble, actual) in enumerate(zip(self.predictions, self.actuals)):
            for node_name, node_pred_ensemble in prediction_ensemble.items():
                if node_pred_ensemble:
                    modeled_emotives = make_modeled_emotives_(ensemble=node_pred_ensemble) # get overall prediction from a single node
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

        # self.pvt_test_result 
        # pprint.pprint(pvt_test_result)
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
        # pprint.pprint(pvt_test_result)
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
        # pprint.pprint(pvt_test_result)
        return pvt_test_result
    
