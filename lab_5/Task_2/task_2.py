import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Вызвана функция '{func.__name__}'")
        print(f"[LOG] Аргументы: позиционные {args}, именованные {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"[LOG] Функция '{func.__name__}' вернула результат: {result}\n")
        return result
        
    return wrapper

@logger
def add_numbers(a, b):
    return a + b

@logger
def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"

add_numbers(5, 7)
greet("Иван", greeting="Здравствуйте")