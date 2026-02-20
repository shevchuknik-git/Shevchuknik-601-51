from math import *

radius = 42
pi = 3.1415926
area = pi * radius**2
print("Площадь круга:", round(area, 4))

point_1 = (23, 34)
distance_1 = sqrt(point_1[0]**2 + point_1[1]**2)
print("Точка 1 (23, 34):", distance_1 <= radius)

point_2 = (30, 30)
distance_2 = sqrt(point_2[0]**2 + point_2[1]**2)
print("Точка 2 (30, 30):", distance_2 <= radius)