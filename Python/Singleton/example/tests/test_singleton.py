import unittest
from src import Singleton

class TestSingleton(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSingleton, self).__init__(*args, **kwargs)
        Singleton()  # Ensure the singleton instance is created before tests run
        pass

    def test_get_singleton_id(self):
        print("Testing Singleton get_id method...")
        instance = Singleton.get_instance()
        id = instance.get_id()
        self.assertIsNotNone(id, "get_id should return an id, but got None.")
        self.assertEqual(id, instance.get_id(), "get_id should return the same id for the same instance.")

    def test_get_singleton_instance(self):
        print("Testing Singleton get_instance method...")
        instance = Singleton.get_instance()
        self.assertIsNotNone(instance, "get_instance should return an instance, but got None.")
    
if __name__ == "__main__":
    unittest.main()
