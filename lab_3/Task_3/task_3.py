def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True

a = 245690
b = 245756

for x in range(a, b + 1):
    if prime(x):
        id = x - a + 1
        print(f'{id} {x}')