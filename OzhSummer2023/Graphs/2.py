import vectors as vc


n = int(input("Сколько вершин? >> "))
graph = [list(map(int, input(f"Координаты {i + 1} вершины >> ").split())) for i in range(n)]
k = list(map(int, input("Вершина К >> ").split()))
mins = None
Kvc = vc.Vector2D(k[0], k[1])
for i in range(n):
    a = vc.Vector2D(graph[i][0], graph[i][1])
    if mins == None:
        mins = (Kvc - a).magnitude
    elif mins > (Kvc - a).magnitude:
        mins = (Kvc - a).magnitude
print(round(mins, 2))