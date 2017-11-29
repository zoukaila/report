import logging
import settings

from config import CONFIGS
from task import Task

class Launcher:
    def __init__(self):
        pass

    def start(self, start, end):
        logging.info('Started processing configs, %d in total', len(CONFIGS))

        for config in CONFIGS:
            logging.info('config - %r', config)

            for i in range(settings.MAX_TASK_RETRY_TIMES):
                try:
                    Task.create_task(config).run(start, end)
                except Exception as err:
                    logging.error('Unexpected exception: %r', err)
                    if i == settings.MAX_TASK_RETRY_TIMES - 1:
                        raise
                    else:
                        logging.error('retry # %d', (i + 1))
                else:
                    break
