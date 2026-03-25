from abc import ABC, abstractmethod

class ICharactor(ABC):
    def __init__(self, name: str):
        self._name = name

    @abstractmethod
    def introduce(self):
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def greeting(self):
        raise NotImplementedError("Subclasses must implement this method.")
    
    def get_name(self):
        return self._name


class NPC(ICharactor):
    def introduce(self):
        print(f"i'm {self._name}, a friendly NPC.")
    
    def greeting(self):
        print(f"{self._name} says: Hello, traveler!")

class Enemy(ICharactor):
    def introduce(self):
        print(f"i'm {self._name}, a dangerous Enemy.")
    
    def greeting(self):
        print(f"{self._name} growls: Prepare to fight!")