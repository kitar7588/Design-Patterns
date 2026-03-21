class Singleton:
    _instance = None
    id = None

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.id = id(self)
        pass

    def get_id(self):
        return self.id