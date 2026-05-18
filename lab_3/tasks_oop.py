import itertools

# ==========================================
# Задача 1: Комбинаторика с ограничениями
# ==========================================
class CombinatoricsSolver:
    """
    Класс для генерации и подсчета кодов по заданным правилам.
    Обобщает алгоритм: позволяет задать любой алфавит, длину кода, 
    особый символ и символ, с которым он не может стоять рядом.
    """
    def __init__(self, alphabet: str, length: int, special_char: str, forbidden_neighbor: str):
        self.alphabet = alphabet
        self.length = length
        self.special_char = special_char
        self.forbidden_neighbor = forbidden_neighbor

    def solve(self) -> int:
        """
        Возвращает количество валидных комбинаций.
        
        Тест для короткого слова из 3 букв 'АЕЙ', где 'Й' не стоит рядом с 'Е',
        не стоит по краям и встречается не более 1 раза.
        >>> solver = CombinatoricsSolver('АЕЙ', 3, 'Й', 'Е')
        >>> solver.solve()
        9
        """
        total = 0
        for code in itertools.product(self.alphabet, repeat=self.length):
            s = ''.join(code)
            if s.count(self.special_char) <= 1:
                if s[0] != self.special_char and s[-1] != self.special_char:
                    if (self.forbidden_neighbor + self.special_char) not in s and \
                       (self.special_char + self.forbidden_neighbor) not in s:
                        total += 1
        return total


# ==========================================
# Задача 2: Подсчет единиц в двоичной записи
# ==========================================
class BinaryExpressionSolver:
    """
    Класс для работы с двоичным представлением математических выражений.
    """
    def __init__(self, value: int):
        self.value = value

    def count_ones(self) -> int:
        """
        Возвращает количество единиц в двоичной записи числа.
        
        Тест для небольшого выражения: 8**2 + 4**1 + 26 - 1 = 93.
        93 в двоичной системе это 1011101 (содержит 5 единиц).
        >>> solver = BinaryExpressionSolver(8**2 + 4**1 + 26 - 1)
        >>> solver.count_ones()
        5
        """
        return bin(self.value).count('1')


# ==========================================
# Задача 3: Поиск простых чисел в диапазоне
# ==========================================
class PrimeRangeFinder:
    """
    Класс для поиска простых чисел в заданном отрезке.
    """
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    @staticmethod
    def is_prime(n: int) -> bool:
        """
        Проверяет, является ли число простым.
        
        >>> PrimeRangeFinder.is_prime(7)
        True
        >>> PrimeRangeFinder.is_prime(10)
        False
        >>> PrimeRangeFinder.is_prime(1)
        False
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def find_primes(self) -> list:
        """
        Возвращает список кортежей (id, prime_number), где id - порядковый номер 
        (начиная с 1) от начала заданного диапазона.
        
        >>> finder = PrimeRangeFinder(10, 15)
        >>> finder.find_primes()
        [(2, 11), (4, 13)]
        """
        result = []
        for x in range(self.start, self.end + 1):
            if self.is_prime(x):
                result.append((x - self.start + 1, x))
        return result


# ==========================================
# Запуск тестов и решений
# ==========================================
if __name__ == "__main__":
    import doctest
    
    print("--- Запуск Doctest ---")
    doctest.testmod(verbose=True)
    
    print("\n--- Результаты исходных задач ---")
    
    task1 = CombinatoricsSolver('АНДРЕЙ', 6, 'Й', 'Е')
    print(f"Задача 1 (Количество кодов): {task1.solve()}")
    
    task2 = BinaryExpressionSolver(8**2020 + 4**2017 + 26 - 1)
    print(f"Задача 2 (Количество единиц): {task2.count_ones()}")
    
    task3 = PrimeRangeFinder(245690, 245756)
    print("Задача 3 (Простые числа):")
    for prime_id, prime_val in task3.find_primes():
        print(f"{prime_id} {prime_val}")