import matplotlib.pyplot as plt
import numpy as np

def draw_polygon(ax, sides, length, center_x, center_y, rotation=0):
    """Рисует правильный многоугольник."""
    angle = 2 * np.pi / sides
    x = [center_x + length * np.cos(i * angle + rotation) for i in range(sides + 1)]
    y = [center_y + length * np.sin(i * angle + rotation) for i in range(sides + 1)]
    ax.plot(x, y, color='black')

def recursive_polygons(ax, sides, length, center_x, center_y, rotation, levels):
    """Рекурсивно рисует последовательность правильных многоугольников."""
    if levels == 0:
        return
    else:
        # Рисуем текущий многоугольник
        draw_polygon(ax, sides, length, center_x, center_y, rotation)

        # Находим координаты вершин следующего многоугольника
        angle = 2 * np.pi / sides
        new_x = [center_x + length * np.cos(i * angle + rotation + angle / 2) for i in range(sides)]
        new_y = [center_y + length * np.sin(i * angle + rotation + angle / 2) for i in range(sides)]

        # Рекурсивно рисуем следующий многоугольник внутри текущего
        for i in range(sides):
            recursive_polygons(ax, sides, length / 2, new_x[i], new_y[i], rotation + angle, levels - 1)

# Пример использования
# Настраиваем начальные параметры
initial_sides = 6  # Начальное количество сторон (шестиугольник)
initial_length = 100  # Длина стороны начального многоугольника
initial_rotation = 0  # Начальный угол поворота

levels = 3  # Количество уровней рекурсии

# Создаем график
fig, ax = plt.subplots()

# Рисуем последовательность правильных многоугольников
recursive_polygons(ax, initial_sides, initial_length, 0, 0, initial_rotation, levels)

# Настраиваем параметры графика
ax.set_aspect('equal', adjustable='datalim')
ax.axis('off')

# Показываем график
plt.show()
