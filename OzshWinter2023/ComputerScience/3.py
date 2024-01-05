from math import sqrt
x1, y1 = map(float, input("x1, y1 => ").split())
x2, y2 = map(float, input("x2, y2 => ").split())
x3, y3 = map(float, input("x3, y3 => ").split())
e = float(input("Погрешность => "))


h_A = abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) / sqrt((x2 - x1)**2 + (y2 - y1)**2)
minS = sqrt((abs(x2 - x3) - sqrt(2)/2 * e)**2 + (abs(y2 - y3) - e)**2) * (h_A - 2 * e) / 2
maxS = sqrt((abs(x2 - x3) + sqrt(2)/2 * e)**2 + (abs(y2 - y3) + e)**2) * (h_A + 2 * e) / 2
print("Минимальная площадь:", minS)
print("Максимальная площадь:", maxS)

# пример: 
# 0 0
# 5 0
# 2.5 4.3301270189221932338186158537647
# 0.5
# Вывод:
# Минимальная площадь: 14.62115620384703
# Максимальная площадь: 29.9023897547921