print("Выражение 1:")
print ("Введите a, b, c, d для R1")
(a11, b11, c11, d11) = map(int, input().split())
print ("Введите a, b, c, d для R2")
(a12, b12, c12, d12) = map(int, input().split())

print("Выражение 2:")
print ("Введите a, b, c, d для R1")
(a21, b21, c21, d21) = map(int, input().split())
print ("Введите a, b, c, d для R2")
(a22, b22, c22, d22) = map(int, input().split())

first = (a11 * b11 + c11 * d11) / (a12 * b12 + c12 * d12)
second = (a21 * b21 + c21 * d21) / (a22 * b22 + c22 * d22)

if first == second:
    print("Они равны")
else:
    print("Превое выражение больше второго" if first > second else "Второе выражение больше первого.")