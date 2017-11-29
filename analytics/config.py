import bson
import datetime
import json
import logging
import settings

from storage import Storage

def __init_config():
    storage = Storage.get_instance()
    configs = storage.find('reportconfigs')
    if configs.count() == 0:
        logging.warning('Cannot find any report config, will insert a mock one for testing')
        storage.insert_one('reportconfigs', {
            'app_id': bson.ObjectId('5a159366049a875c9ec2daeb'),
            'metric': '# of sessions',
            'module': 'nodemessages',
            'aggregation_criteria': json.dumps([
                {'$match': {'info.payload.type': 'agentRank'}},
                {'$group': {'_id': None, 'avg': {'$avg': "$info.payload.rank_score_bot"}}}
            ]),
            'created': datetime.datetime.now(),
            'updated': datetime.datetime.now()
        })
        configs = storage.find('reportconfigs')

    return list(configs)

CONFIGS = __init_config()
CONFIG_KEY_APP_ID ='app_id'
CONFIG_KEY_METRIC = 'metric'
CONFIG_KEY_MODULE = 'module'
CONFIG_KEY_AGGREGATE = 'aggregation_criteria'
