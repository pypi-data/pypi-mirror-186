# AnyLog-API
The AnyLog API is intended to act an easy-to-use interface between AnyLog and third-party applications via REST.

[deploy_node.py](deployments/python_rest/deploy_node.py) provides code to deploy AnyLog via REST when given a [configuration file](configurations/). 
The configuration file can be either _.env_ or _YAML_; as generated when creating it with [deployment scripts](https://github.com/AnyLog-co/deployments/tree/master/deployment_scripts). 


### Code Breakdown
* [anylog_connector](python_rest/src/anylog_connector.py) - Class that declares connection to AnyLog, used for
_GET_, _PUT_ and _POST_.
* [generic get](python_rest/src/generic_get_calls.py)
  * check status
  * get (AnyLog) dictionary
  * view event log 
  * view error log 
  * view network information
  * `get hostname` 
  * `get processes`
  * `help`
* [generic post](python_rest/src/generic_post_calls.py)
  * add param to (AnyLog) dictionary 
  * network connectivity connect
  * run scheduler 
  * setting buffer / streamer 
  * `run operator` 
  * `run publisher`
* [generic data](python_rest/src/generic_data_calls.py)
  * `run mqtt client`
  * data partitioning
  * insert data via _POST_ or _PUT_
  * query data 
* [blockchain calls](python_rest/src/blockchain_calls.py)
  * blockchain syncing
  * `blockchain get`
  * prepare policy
  * post policy 
* [database calls](python_rest/src/database_calls.py)
  * `get databases`
  * `get tables`
  * connect to database 
  * create table
* [find location](python_rest/src/find_location.py) - code to get the geolocation of the node being accesseed 



## Node Setup
1. Download AnyLog-API
```shell
cd $HOME ; git clone https://github.com/AnyLog-co/AnyLog-API
```

2. Install Requirements
   * ast 
   * dotenv 
   * json 
   * os 
   * requests 
   * yaml
```shelll
python3.9 -m pip install -r $HOME/AnyLog-API/python_rest/requirements.txt
 ```


## Base Code
```python3
import os
import sys

ROOT_DIR = os.path.expandvars(os.path.expanduser(__file__)).split('README.md')[0]
sys.path.insert(0, os.path.join(ROOT_DIR, 'python_rest', 'src'))

from anylog_connector import AnyLogConnector

# connect to AnyLog 
anylog_conn = AnyLogConnector(conn='127.0.0.1:32049', auth='username,password', timeout=30)

"""
using methods in python_rest, easily communicate with the AnyLog node via REST 
"""
```