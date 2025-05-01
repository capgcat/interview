from pymongo import MongoClient, UpdateOne

class MongoConnection():
    __client = None
    __database = "interview"

    def __init__(self, connection_params) -> None:
        self.connection_params = connection_params
        self.create_conn(connection_params)

    def create_conn(self, connection_params):
        if connection_params.get('connected_on') == 'mongo_cluster':
            self.__client = MongoClient(connection_params.get('mongodb_uri'))
        return self.__client

    @property
    def client(self):
        return self.__client

    @property
    def db(self):
        return self.__client[self.__database]

    @property
    def default_db(self):
        return self.__database

    def close_conn(self) -> str:
        self.__client.close()
        return "connection closed"
