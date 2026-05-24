import functools

class CountCalls:
    """Декоратор на основе класса, считающий количество вызовов функции."""
    
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"[LOG] Функция {self.func.__name__} вызвана {self.num_calls} раз(а)")
        return self.func(*args, **kwargs)

@CountCalls
def greet(name):
    return f"Привет, {name}!"

print(greet("Алексей"))
print(greet("Мария"))