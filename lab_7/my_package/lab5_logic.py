import functools

def make_line_reader(filename):
    """Замыкание для построчного чтения файла."""
    file = open(filename, 'r', encoding='utf-8')
    
    def get_next_line():
        line = file.readline()
        if not line:
            file.close()
            return None
        return line.strip()
        
    return get_next_line

def singleton(cls):
    """Декоратор класса, превращающий его в Singleton (Одиночку)."""
    instances = {}
    
    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
        
    return get_instance

if __name__ == "__main__":
    @singleton
    class DatabaseConnection:
        def __init__(self):
            print("Инициализация подключения к БД...")
            
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"db1 и db2 - один и тот же объект? {db1 is db2}")