import functools

def singleton(cls):
    """Декоратор класса, превращающий его в Singleton."""
    instances = {}
    
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
        
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        print("Инициализация подключения к БД...")

db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(f"db1 и db2 - один и тот же объект? {db1 is db2}")