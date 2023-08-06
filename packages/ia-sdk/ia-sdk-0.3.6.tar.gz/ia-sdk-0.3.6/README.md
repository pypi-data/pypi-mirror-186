# GAIuS™ Python SDK
A Python SDK for Intelligent Artifacts' GAIuS™ agents.

## What is GAIuS™?
GAIuS™ is an Artificial General Intelligence framework for rapidly building machine intelligence solutions for any problem domain.

## What is IA's Python SDK?
This package, ia-sdk-python, is a software development kit for interacting with IA's GAIuS agents from Python.  It provides useful tools and services.

## Install
`pip install ia-sdk`

Provides:

    - GenomeInfo
    - AgentClient
    - BackTesting

#### To use GenomeInfo:

You will need to download your gaius_agent's genome file from your Intelligent Artifacts account.

~~~
from ia.gaius.GenomeInfo import Genome
import json

genome_topology = json.loads(genome_json_string)
genome = Genome(genome_topology)
~~~

If you want to have the topology displayed, you need to install cyjupter:

`pip3 install cyjupyter`


##### The useful functions are:
~~~
genome.agent - returns the name of the agent.
    ex: 'focusgenie'

genome.get_nodes() - returns 2-tuple of primitives and manipulatives genomic data.

genome.get_actions() - returns dictionary of primitives with lists of action IDs.
    ex: {'P1': ['ma23b1323',
                'm390d053c']}

genome.get_action_manipulatives() - returns a list of action manipulative IDs.
    ex: ['m390d053c',
         'ma23b1323']

genome.get_primitive_map() - returns a dictionary of primitive names to primitive IDs.
    ex: {'P1': 'p464b64bc'}

genome.get_manipulative_map() - returns a dictionary of manipulative IDs to manipulative names.
    ex: {'m390d053c': 'ACTIONPath',
         'ma23b1323': 'ACTIONPath',
         'mcd6d4d68': 'negateContext',
         'm40aaf174': 'vectorFilter',
         'med2ed537': 'vectorPassthrough',
         'm89aa2c7e': 'reduceVectorsBySubtraction'}

genome.display() - graphically displays the topology.
~~~



#### To use AgentClient:

You will need to have an active bottle running on Intelligent Artifacts.  The bottle's information such as 'name' and secrete 'api_key' can be found in your IA account.

If on IA cloud:

~~~
from ia.gaius.agent_client import AgentClient

bottle_info = {'api_key': 'ABCD-1234',
               'name': 'gaius-agent',
               'domain': 'intelligent-artifacts.com',
               'secure': True}

test_bottle = AgentClient(bottle_info)
test_bottle
~~~


If local:
(Note: local, on-premises, on-board, at-the-edge, etc. usage requires licensing from Intelligent Artifacts. Send email to team@intelligent-artifacts.com for licensing support.)
~~~
from ia.gaius.agent_client import AgentClient

bottle_info = {'api_key': 'ABCD-1234',
               'name': 'gaius-agent',
               'domain': ':8181',
               'secure': False}

test_bottle = AgentClient(bottle_info)
test_bottle
~~~

Prior to utilizing the bottle, you must establish a connection between the client and bottle through the use of the connect method:

~~~
test_bottle.connect()
~~~

Note, this will download a copy of the gaius_agent's genome. Alternatively, you can manually inject your gaius_agent's genome into the bottle and connect in this manner:

~~~
test_bottle.inject_genome(genome)
~~~

Wait for return status.

Once you have a running gaius_agent, set ingress and query nodes by passing the node names in a list:

~~~
test_bottle.set_ingress_nodes(['P1'])
test_bottle.set_query_nodes(['P1'])
~~~

Send data to bottle:

~~~
data = {"strings": ["Hello"], "vectors": [], "determinants": []}
test_bottle.observe(data)
~~~

Query the bottle nodes:

~~~
print(test_bottle.show_status())
predictions = test_bottle.get_predictions()
~~~


When sending classifications to a gaius_agent, it is best practice to send the classification as a singular symbol in the last event of a sequence.  This allows for querying the last event in the prediction's 'future' field for the answer.  The classification, though, should be sent to all the query nodes along with the ingress nodes.  The `observe_classification` function of the `AgentClient` class does that for us:

~~~
data = {"strings": ["World!"], "vectors": [], "determinants": []}
test_bottle.observe_classification(data)
~~~

#### To use Backtesting:

There are 3 built-in backtesting reports:

    - classification:
        - Train and predict a string value to be a classification of observed data.
    - utility - polarity:
        - Polarity is basically a +/- binary classification test using the prediction's 'utility' value.  It scores correct if the polarity of the prediction matches the polarity of the expected.
    - utility - value:
        - Value tests for the actual predicted value against the expected and scores correct if within a provided `tolerance_threshold`.

For each, the observed data can be a sequence of one or more events, containing any vectors or strings.
