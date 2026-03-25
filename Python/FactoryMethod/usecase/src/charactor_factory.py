from abc import ABC, abstractmethod
from .charactor import NPC, Enemy

class CharactorFactory(ABC):
    @abstractmethod
    def create_charactor(self, name: str):
        pass

    def spawn_charactor(self, name: str = "noBody"):
        return self.create_charactor(name)

class NPCFactory(CharactorFactory):
    def create_charactor(self, name: str = "noBody"):
        return NPC(name)

class EnemyFactory(CharactorFactory):
    def create_charactor(self, name: str = "noBody"):
        return Enemy(name)