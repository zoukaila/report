from pymongo import command_cursor, cursor, MongoClient, results

import settings

class Storage:
    class __Storage:
        def __init__(self):
            # TODO: how to manage connections? pooling, close, reuse...
            uri = settings.MONGODB_URI
            client = MongoClient(uri)
            self.__db = client.ChatFlow

        def find(self, col_name, filter_criterias={}) -> cursor.Cursor:
            return self.__db.get_collection(col_name).find(filter_criterias)

        def insert_one(self, col_name, doc):
            return self.__db.get_collection(col_name).insert_one(doc)

        def insert_many(self, col_name, docs) -> results.InsertManyResult:
            return self.__db.get_collection(col_name).insert_many(docs)

        def aggregate(self, col_name, pipeline) -> command_cursor.CommandCursor:
            return self.__db.get_collection(col_name).aggregate(pipeline)

    __singleton = None

    def __init__(self):
        raise SyntaxError('Please instantiate using get_instance')

    @classmethod
    def get_instance(cls):
        # TODO: not thread safe yet.
        if not cls.__singleton:
            cls.__singleton = cls.__Storage()
        return cls.__singleton
