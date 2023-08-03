import colorama as cl
import queue

cl.init()

n = int(input("Сколько вершин? >> "))
graph = {}
for i in range(n):
    v = input("Вершина >> ")
    lv = input("С какими связана >> ").split()
    graph[v] = lv


node = list(graph.keys())[0]
visited, q, space = set(), queue.Queue(), [node]
visited.add(node)
q.put(node)
while not q.empty():
    vertex = q.get()
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            visited.add(neighbour)
            q.put(neighbour)
            space.append(neighbour)

if len(space) == n:
    print(cl.Back.GREEN + cl.Style.BRIGHT + "Связан" + cl.Style.RESET_ALL)
else:
    print(cl.Back.RED + cl.Style.BRIGHT + "Не связан" + cl.Style.RESET_ALL)