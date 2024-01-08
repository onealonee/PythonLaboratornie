import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_polygon(vertices):
    """
    Отрисовка многоугольника по заданным вершинам
    """
    polygon = patches.Polygon(vertices, closed=True, edgecolor='black')
    plt.gca().add_patch(polygon)


def build_polygon_sequence(level, vertices):
    """
    Построение последовательности многоугольников с использованием рекурсии
    """
    if level == 0:
        # Базовый случай: отрисовка первоначального многоугольника
        draw_polygon(vertices)
    else:
        # Построение вершин текущего многоугольника
        new_vertices = build_new_vertices(vertices)

        # Отрисовка текущего многоугольника
        draw_polygon(new_vertices)

        # Рекурсивный вызов для следующего уровня
        build_polygon_sequence(level - 1, new_vertices)


def build_new_vertices(previous_vertices):
    """
    Построение вершин нового многоугольника на основе предыдущего
    """
    new_vertices = []
    num_vertices = len(previous_vertices)

    for i in range(num_vertices):
        # Берем середину между текущей и следующей вершиной
        x = (previous_vertices[i][0] + previous_vertices[(i + 1) % num_vertices][0]) / 2
        y = (previous_vertices[i][1] + previous_vertices[(i + 1) % num_vertices][1]) / 2
        new_vertices.append((x, y))

    return new_vertices


# Задаем первоначальный многоугольник (шестиугольник)
initial_vertices = [(1, 0), (0.5, 0.87), (-0.5, 0.87), (-1, 0), (-0.5, -0.87), (0.5, -0.87)]

# Задаем уровень рекурсии
recursion_level = 10

# Отрисовываем последовательность многоугольников
build_polygon_sequence(recursion_level, initial_vertices)

# Настраиваем график
plt.axis('equal')
plt.show()
