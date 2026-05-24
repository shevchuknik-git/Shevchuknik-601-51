import multiprocessing
import time
from itertools import islice

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def parallel_prime_gen(chunk_size=10000):
    """Параллельный генератор простых чисел."""
    num = 2
    with multiprocessing.Pool() as pool:
        while True:
            candidates = range(num, num + chunk_size)
            
            results = pool.map(is_prime, candidates)
            
            for candidate, is_p in zip(candidates, results):
                if is_p:
                    yield candidate
            
            num += chunk_size

def sequential_prime_gen():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

if __name__ == '__main__':
    N = 50000  
    
    print(f"Генерация первых {N} простых чисел...")
    
    start_time = time.time()
    seq_primes = list(islice(sequential_prime_gen(), N))
    seq_time = time.time() - start_time
    print(f"Последовательная версия: {seq_time:.4f} сек")
    
    start_time = time.time()
    par_primes = list(islice(parallel_prime_gen(chunk_size=20000), N))
    par_time = time.time() - start_time
    print(f"Параллельная версия: {par_time:.4f} сек")
    
    assert seq_primes == par_primes, "Результаты не совпадают!"
    
    if par_time < seq_time:
        print(f"\nУскорение составило: в {seq_time / par_time:.2f} раз(а)!")
    else:
        print("\nНа малых данных накладные расходы на создание процессов превышают выгоду.")