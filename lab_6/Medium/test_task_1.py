import pytest
from itertools import islice
from task_1 import prime_gen

def test_first_prime():
    """Тест проверяет первое простое число."""
    gen = prime_gen()
    assert next(gen) == 2

def test_first_five_primes():
    """Тест проверяет первые 5 простых чисел."""
    gen = prime_gen()
    primes = [next(gen) for _ in range(5)]
    assert primes == [2, 3, 5, 7, 11]

def test_primes_slice():
    """Тест проверяет срез из 10 чисел с помощью itertools.islice."""
    gen = prime_gen()
    primes = list(islice(gen, 10))
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_specific_prime():
    """Тест проверяет, что 20-е простое число равно 71."""
    gen = prime_gen()
    primes = list(islice(gen, 20))
    assert primes[-1] == 71

if __name__ == "__main__":
    pytest.main(["-v", "test_task_1.py"])