def calc(i):
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5
    
    return calc(i - 1) * calc(i - 2) * ((i - 1)**2) / ((i + 1)**3)
print(calc(5))