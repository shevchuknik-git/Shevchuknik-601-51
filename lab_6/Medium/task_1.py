def prime_gen():
    num = 2

    while True:
        prime = True
        
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
                
        if prime:
            yield num
            
        num += 1

if __name__ == "__main__":
    primes = prime_gen()

    print("Первые 10 простых чисел:")
    for _ in range(10):
        print(next(primes), end=" ")
        
    print("\n\nЕще 5 простых чисел:")
    for _ in range(5):
        print(next(primes), end=" ")