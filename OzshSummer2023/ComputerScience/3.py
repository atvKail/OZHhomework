import vectors

(x1, y1) = map(float, input("Введите x и y, считая с левой стороны:\nX1, Y1 >> ").split())
(x2, y2) = map(float, input("\nX2, Y2 >> ").split())
(x3, y3) = map(float, input("\nX3, Y3 >> ").split())
e = float(input("\nЧему равна погрешность? >> "))

Smin = abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) / 2 
for j in range(-1, 2, 2):
    for z in range(-1, 2, 2):
        for n in range(-1, 2 ,2):
            for b in range(-1, 2, 2):
                for v in range(-1, 2, 2):
                    for c in range(-1, 2 ,2):
                        p1 = [x1 + e * j, y1 + e * z]
                        p2 = [x2 + e * n, y2 + e * b]
                        p3 = [x3 + e * v, y3 + e * c]
                        nS = abs((p2[0] - p1[0])*(p3[1] - p1[1]) - (p3[0] - p1[0])*(p2[1] - p1[1])) / 2
                        Smin = nS if Smin > nS else Smin
print("Минимальная площадь: ", Smin)

ot = max(vectors.Vector2D(x1 - x2 - 2 * e, y1 - y2 - 2 * e).magnitude, vectors.Vector2D(x1 - x2 + 2 * e, y1 - y2 - 2 * e).magnitude) / \
    (vectors.Vector2D(x1 - x2, y1 - y2).magnitude)
Smax = (abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1)) / 2) * ot

print("Максимальная площадь: ", Smax)

