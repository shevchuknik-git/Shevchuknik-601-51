def calc(i):
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5
        
    w_prev2 = 0.3
    w_prev1 = -1.5
    
    for k in range(3, i + 1):
        w_current = w_prev1 * w_prev2 * ((k - 1)**2) / ((k + 1)**3)
        
        w_prev2 = w_prev1
        w_prev1 = w_current
        
    return w_prev1
print(calc(5))