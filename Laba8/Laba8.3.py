import matplotlib.pyplot as plt
import numpy as np

def draw_hexagon(ax, center, size):
    """Рисует правильный шестиугольник."""
    angles = np.linspace(0, 2 * np.pi, 7)
    x = center[0] + size * np.cos(angles)
    y = center[1] + size * np.sin(angles)
    ax.plot(x, y, color='black')

def recursive_draw(ax, center, size, levels):
    """Рекурсивно рисует последовательность вложенных шестиугольников."""
    if levels == 0:
        return
    else:
        draw_hexagon(ax, center, size)
        next_size = size / 2
        for i in range(6):
            next_center = (
                center[0] + size * np.cos(2 * np.pi / 6 * i),
                center[1] + size * np.sin(2 * np.pi / 6 * i)
            )
            recursive_draw(ax, next_center, next_size, levels - 1)

# Создаем фигуру и оси
fig, ax = plt.subplots()

# Задаем начальные параметры
initial_center = (0, 0)
initial_size = 100
initial_levels = 3

# Рисуем последовательность вложенных шестиугольников
recursive_draw(ax, initial_center, initial_size, initial_levels)

# Устанавливаем равное соотношение сторон для лучшей визуализации
ax.set_aspect('equal', adjustable='box')

# Показываем график
plt.show()
