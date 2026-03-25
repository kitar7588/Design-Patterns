from abc import ABC, abstractmethod
from .produce import ConcreteProduceA, ConcreteProduceB

class Factory(ABC):
    @abstractmethod
    def create_product(self, id):
        raise NotImplementedError("Subclasses must implement this method")

class ConcreteFactoryA(Factory):
    def create_product(self,id):
        return ConcreteProduceA(id)

class ConcreteFactoryB(Factory):
    def create_product(self,id):
        return ConcreteProduceB(id)
    
