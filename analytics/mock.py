from datetime import datetime
import json

from storage import Storage

def init_report_config():
    Storage.get_instance().insert_one('reportconfigs', {
        'app_id': '23e0e5c0.02eaca',
        'metric_name': 'avg rank score by customers',
        'collection_name': 'nodemessages',
        'aggregation_criterias': json.dumps([
            {'$match': {'info.payload.type': 'agentRank'}},
            {'$group': {'_id': None, 'avg': {'$avg': "$info.payload.rank_score_bot"}}}
        ]),
        'created': datetime.now(),
        'updated': datetime.now()
    })

def main():
    init_report_config()

if __name__ == '__main__':
    main()
