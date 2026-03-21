import unittest
from src.database_connector import DatabaseConnector

class TestDatabaseConnector(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestDatabaseConnector, self).__init__(*args, **kwargs)
        DatabaseConnector()  # Ensure the singleton instance is created before tests run
        pass

    def test_singleton_instance(self):
        print("Testing DatabaseConnector singleton instance...")
        set_of_instances = set(DatabaseConnector.get_instance() for _ in range(5))

        self.assertIsNotNone(DatabaseConnector.get_instance(), "get_instance should return an instance, but got None.")
        self.assertEqual(len(set_of_instances), 1, "get_instance should return the same instance for multiple calls.")
        pass

    def test_connection_id_consistency(self):
        print("Testing DatabaseConnector connection ID consistency...")
        instance1 = DatabaseConnector.get_instance()
        instance2 = DatabaseConnector.get_instance()

        self.assertEqual(instance1.get_connection_id(), instance2.get_connection_id(), "Connection IDs should be the same for the singleton instance.")
        pass

    def test_dbs_consistency(self):
        print("Testing DatabaseConnector DBs consistency...")
        instance = DatabaseConnector.get_instance()
        
        id = instance.get_connection_id()

        dbs = []
        dbs.append(instance.get_first_db())
        dbs.append(instance.get_second_db())

        set_of_different_values = {dbs[0],dbs[1],id}

        self.assertEqual(dbs[0], dbs[1], "DBs should be the same for the singleton instance.")
        self.assertEqual(len(set_of_different_values), 1, "DBs should be the same as the connection ID for the singleton instance.")
        pass

if __name__ == "__main__":
    unittest.main()