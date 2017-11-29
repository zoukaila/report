import config
import json
import logging
import settings

from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from storage import Storage

class Task(ABC):
    def __init__(self, config):
        self.__config = config

    @abstractmethod
    def run(self):
        pass

class AggregateTask(Task):
    def run(self):
        storage = Storage.get_instance()
        aggregate = [
            {'$match': {'registered_at': {'$gte': datetime.now() - timedelta(days=1)}}},
            {'$match': {'info.appId': self.__config[config.CONFIG_KEY_APP_ID]}}
        ]
        aggregate.extend(json.loads(self.__config[config.CONFIG_KEY_AGGREGATE]))
        result = storage.aggregate(self.__config[config.CONFIG_KEY_MODULE], aggregate)
        logging.info('Aggregation result: %r', result)


        storage.insert_many(settings.COL_NAME_AGGR_RESULT, )

        return result
