from .database_connector import DatabaseConnector

if __name__ == "__main__":
    print("Singleton Use Case : Database Connector")
    # --- Verification ---

    # Attempt to create two separate objects
    db1 = DatabaseConnector()
    db2 = DatabaseConnector()

    print(f"Database 1 ID: {db1.get_connection_id()}")
    print(f"Database 2 ID: {db2.get_connection_id()}")

    # Check if they are the exact same object in memory
    print(f"Are they the same instance? {db1 is db2}")