class Singleton:
    _instance = None
    id = None

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance is not None:
            return
        self.id = id(self)
        Singleton._instance = self
        pass
    
    def get_id(self):
        return self.id