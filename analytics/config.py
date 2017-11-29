import logging

from storage import Storage

def __init_config():
    storage = Storage.get_instance()
    configs = storage.find('reportconfigs')
    if configs.count() == 0:
        logging.warning('Cannot find any report config')

    return list(configs)

CONFIGS = __init_config()
CONFIG_KEY_APP_ID = 'app_id'
CONFIG_KEY_METRIC_NAME = 'metric_name'
CONFIG_KEY_COLLECTION_NAME = 'collection_name'
CONFIG_KEY_AGGREGATE = 'aggregation_criterias'
