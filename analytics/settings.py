import os

MONGODB_URI = os.getenv('MONGODB_URI') or 'mongodb://localhost:27017'
DB_NAME = 'ChatFlow'
COL_NAME_AGGR_RESULT = 'reportaggr'
MAX_TASK_RETRY_TIMES = 3
TASK_RETRY_INTERVAL_SEC = 1
