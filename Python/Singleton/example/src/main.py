from src import Singleton

if __name__ == "__main__":
    instance = Singleton()
    id = instance.get_id()
    print(f"Singleton instance ID: {id}")
    second_id = Singleton.get_instance().get_id()
    print(f"Use get_instance got ID: {second_id}")
    print(f"Those ids are the same: {id == second_id}")