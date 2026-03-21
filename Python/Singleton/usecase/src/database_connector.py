import random

class DatabaseConnector:
    _instance = None
    _connection_id = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnector, cls).__new__(cls)
            cls._initialize(cls)
        return cls._instance

    def _initialize(cls):
        cls._randomize_connection_id(cls)
        cls._create_dbs(cls)
        pass

    def _randomize_connection_id(cls):
        cls._connection_id = random.randint(1, 1000)
        pass

    def _create_dbs(cls):
        id = cls._connection_id
        cls.dbs = [id,id]
        pass
    
    #----------
    # Getters
    #----------

    def get_connection_id(self):
        return self._connection_id
    
    def get_first_db(self):
        return self.dbs[0]
    
    def get_second_db(self):
        return self.dbs[1]

    @staticmethod
    def get_instance():
        if DatabaseConnector._instance is None:
            raise Exception("DatabaseConnector instance is not initialized.")
        return DatabaseConnector._instance