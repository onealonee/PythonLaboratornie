def find_next_vertices(vertices, current_vertex, visited):
    next_vertices = [i for i, vertex in enumerate(vertices) if not visited[i] and (vertex[0] == current_vertex[0] or vertex[1] == current_vertex[1])]
    return next_vertices

def restore_order(vertices, current_vertex, visited, result_sequence):
    result_sequence.append(current_vertex)
    visited[current_vertex] = True
    next_vertices = find_next_vertices(vertices, vertices[current_vertex], visited)

    for next_vertex in next_vertices:
        if not visited[next_vertex]:
            restore_order(vertices, next_vertex, visited, result_sequence)

# Ввод координат вершин с клавиатуры
num_vertices = int(input("Введите количество вершин: "))
vertices = []

for i in range(num_vertices):
    x, y = map(int, input(f"Введите координаты вершины {i + 1} (x y): ").split())
    vertices.append((x, y))

# Инициализация
visited = [False] * len(vertices)
result_sequence = []

# Начать восстановление порядка с первой вершины
restore_order(vertices, 0, visited, result_sequence)

# В результате result_sequence будет содержать вершины в правильном порядке
print(result_sequence)
