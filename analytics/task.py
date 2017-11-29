from abc import ABC, abstractmethod
from datetime import datetime
import json
import logging

import config
import settings
from storage import Storage

class Task(ABC):
    def __init__(self, config):
        self._config = config

    @abstractmethod
    def run(self, start, end):
        pass

    @classmethod
    def create_task(cls, config):
        # TODO: currently we only support AggregateTask.
        return AggregateTask(config)

class AggregateTask(Task):
    def run(self, start, end):
        storage = Storage.get_instance()
        aggregate = [
            {'$match': {'registered_at': {'$gte': start, '$lt': end}}},
            {'$match': {'info.appId': self._config[config.CONFIG_KEY_APP_ID]}}
        ]
        aggregate.extend(json.loads(self._config[config.CONFIG_KEY_AGGREGATE]))
        aggr_result = storage.aggregate(self._config[config.CONFIG_KEY_COLLECTION_NAME], aggregate)

        if aggr_result.alive:
            current_time = datetime.now()
            transformed_result = [{
                'app_id': self._config[config.CONFIG_KEY_APP_ID],
                'metric_id': self._config['_id'],
                'group': line['_id'],
                'key': key,
                'value': value,
                'start': start,
                'end': end,
                'created': current_time,
                'updated': current_time
            } for line in aggr_result for key,value in line.items() if key != '_id' ]

            storage.insert_many(settings.COL_NAME_AGGR_RESULT, transformed_result)
