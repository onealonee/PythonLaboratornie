import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_polygon(vertices):
    """
    Отрисовка многоугольника по заданным вершинам
    """
    polygon = patches.Polygon(vertices, closed=True, edgecolor='black')
    plt.gca().add_patch(polygon)

def build_polygon_sequence(level, vertices, ratio):
    """
    Построение последовательности правильных многоугольников с использованием рекурсии
    """
    if level == 0:
        # Базовый случай: отрисовка последнего многоугольника
        draw_polygon(vertices)
    else:
        new_vertices = build_new_vertices(vertices, ratio)
        draw_polygon(new_vertices)
        build_polygon_sequence(level - 1, new_vertices, ratio)

def build_new_vertices(previous_vertices, ratio):
    """
    Построение новых вершин многоугольника на основе предыдущих и заданного отношения
    """
    new_vertices = []
    num_vertices = len(previous_vertices)

    for i in range(num_vertices):
        # Текущая вершина
        current_vertex = previous_vertices[i]
        # Следующая вершина
        next_vertex = previous_vertices[(i + 1) % num_vertices]
        # Точка деления стороны в заданном отношении
        new_x = current_vertex[0] + ratio * (next_vertex[0] - current_vertex[0])
        new_y = current_vertex[1] + ratio * (next_vertex[1] - current_vertex[1])
        new_vertices.append((new_x, new_y))

    return new_vertices

# Задаем первоначальный многоугольник (шестиугольник)
initial_vertices = [(1, 0), (0.5, 0.87), (-0.5, 0.87), (-1, 0), (-0.5, -0.87), (0.5, -0.87)]

# Задаем уровень рекурсии
recursion_level = 100

# Задаем отношение деления стороны (можете изменить по своему усмотрению)
division_ratio = 0.8

# Отрисовываем последовательность многоугольников
build_polygon_sequence(recursion_level, initial_vertices, division_ratio)

# Настраиваем график
plt.axis('equal')
plt.show()
