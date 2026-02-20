from itertools import *

num = ['1','2','3','4','5']
ops = ['+','-','*']

for comb in product(ops, repeat=4):
    exp = f"(({num[0]}{comb[0]}{num[1]}{comb[1]}{num[2]}){comb[2]}{num[3]}){comb[3]}{num[4]}"
    if eval(exp) == 25:  
        print(exp, '= 25')