from unittest import TestCase
from usecase.src import NPCFactory, EnemyFactory, CharactorFactory

def spawn_charactor(factory: CharactorFactory, name: str):
    charactor = factory.create_charactor(name)
    return charactor

class TestCharactorFactory(TestCase):
    def test_npc_factory_create_charactor(self):
        print("test NPCFactory's create_charactor")
        factory = NPCFactory()
        charactor_name = "John"
        charactor = factory.spawn_charactor(charactor_name)
        self.assertIsNotNone(charactor, "create_charactor should return a charactor instance, but got None.")
        self.assertEqual(charactor.get_name(), charactor_name, "create_charactor should set the name of the charactor correctly.")
        self.assertIsNotNone(charactor.introduce, "NPC should have an introduce method.")
        self.assertIsNotNone(charactor.greeting, "NPC should have a greeting method.")
        pass

    def test_enemy_factory_create_charactor(self):
        print("test EnemyFactory's create_charactor")
        factory = EnemyFactory()
        charactor_name = "Goblin"
        charactor = factory.spawn_charactor(charactor_name)
        self.assertIsNotNone(charactor, "create_charactor should return a charactor instance, but got None.")
        self.assertEqual(charactor.get_name(), charactor_name, "create_charactor should set the name of the charactor correctly.")
        self.assertIsNotNone(charactor.introduce, "Enemy should have an introduce method.")
        self.assertIsNotNone(charactor.greeting, "Enemy should have a greeting method.")
        pass
       
