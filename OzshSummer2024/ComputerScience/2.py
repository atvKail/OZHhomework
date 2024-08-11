import matplotlib.pyplot as plt
from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Коллинеарные
    elif val > 0:
        return 1  # По часовой стрелке
    else:
        return 2  # Против часовой стрелки

def convex_hull(points):
    n = len(points)
    if n < 3:
        return None
    
    # Ищем самую левую точку
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l = i
    
    hull = []
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
        p = q
        if p == l:
            break
    
    return hull

def plot_hull(points, hull):
    plt.figure()
    x, y = zip(*points)
    plt.plot(x, y, 'o')
    
    hull_points = hull + [hull[0]]
    hx, hy = zip(*hull_points)
    plt.plot(hx, hy, 'r-')
    plt.fill(hx, hy, 'r', alpha=0.2)
    
    plt.title('Convex Hull')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

def main():
    # Ввод данных
    n = int(input("Введите количество вершин: "))
    points = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Построение выпуклой оболочки
    hull = convex_hull(points)
    if hull is None:
        print("Невозможно построить выпуклую оболочку для менее чем 3 точек.")
        return
    
    # Вычисление длины забора
    length = sum(distance(hull[i], hull[(i + 1) % len(hull)]) for i in range(len(hull)))
    
    # Вывод результата
    print("Координаты вершин забора:")
    for p in hull:
        print(p)
    
    print(f"Длина забора: {length}")
    
    # Построение графика
    plot_hull(points, hull)

if __name__ == "__main__":
    main()
