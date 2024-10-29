from collections import defaultdict, deque

def find_eulerian_path(pieces):
    # Построение графа
    graph = defaultdict(list)
    degree = defaultdict(int)
    
    for u, v in pieces:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Проверка количества вершин с нечетной степенью
    start = None
    odd_vertices = 0
    for node in degree:
        if degree[node] % 2 != 0:
            odd_vertices += 1
            start = node
    
    if odd_vertices != 0 and odd_vertices != 2:
        return "Невозможно составить цепочку"
    
    if start is None:
        start = pieces[0][0]
    
    # Функция для нахождения эйлерова пути или цикла
    def find_path(start):
        stack = [start]
        path = []
        local_graph = graph.copy()
        
        while stack:
            u = stack[-1]
            if local_graph[u]:
                v = local_graph[u].pop()
                local_graph[v].remove(u)
                stack.append(v)
            else:
                path.append(stack.pop())
        return path[::-1]
    
    path = find_path(start)
    
    if len(path) != len(pieces) + 1:
        return "Невозможно составить цепочку"
    
    return [(path[i], path[i+1]) for i in range(len(path) - 1)]

# Входные данные
n = int(input("Введите количество костей домино: "))
pieces = [tuple(map(int, input().split())) for _ in range(n)]

result = find_eulerian_path(pieces)

if isinstance(result, str):
    print(result)
else:
    for p in result:
        print(f"{p[0]}-{p[1]}")
