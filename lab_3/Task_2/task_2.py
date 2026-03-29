def bin_ones():
    value = 8**2020 + 4**2017 + 26 - 1
    return bin(value).count('1')
print('Количество единиц:', bin_ones())