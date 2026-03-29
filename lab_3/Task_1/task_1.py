from itertools import*

def comb():
    total = 0
    for code in product('АНДРЕЙ', repeat=6):
        s = ''.join(code)
        if s.count('Й') <= 1:
            if s[0] != 'Й' and s[-1] != 'Й':
                if 'ЕЙ' not in s and 'ЙЕ' not in s:
                    total += 1
    return total
print(comb())