from abc import ABC, abstractmethod

class IProduce(ABC):
    def __init__(self, id: int):
        self._id = id
        pass

    @abstractmethod
    def get_id(self):
        raise NotImplementedError("Subclasses must implement this method")


class ConcreteProduceA(IProduce):
    def get_id(self):
        return self._id
    

class ConcreteProduceB(IProduce):
    def get_id(self):
        return self._id

