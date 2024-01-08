import matplotlib.pyplot as plt
import numpy as np


def draw_circle(x, y, size):
    """
    Отрисовка окружности в заданных координатах и размере
    """
    circle = plt.Circle((x, y), size, edgecolor='black', facecolor='none')
    plt.gca().add_patch(circle)


def draw_recursive_circles(x, y, size, levels):
    """
    Рекурсивная функция для отрисовки окружностей вокруг каждой окружности
    """
    if levels == 0:
        return
    else:
        # Отрисовка текущей окружности
        draw_circle(x, y, size)

        # Рекурсивный вызов для каждой из 4 окружностей вокруг текущей
        new_size = size * 0.5
        angles = np.linspace(0, 2 * np.pi, 5, endpoint=False)
        for i in range(1, 5):
            angle = i * (2 * np.pi / 4)
            if levels == 1:
                # Уменьшаем расстояние между центрами только на первом уровне
                new_x = x + size * 4 * np.cos(angle)
                new_y = y + size * 4 * np.sin(angle)
            else:
                # Оставляем прежнее расстояние на последующих уровнях
                new_x = x + size * 2 * np.cos(angle)
                new_y = y + size * 2 * np.sin(angle)
            draw_recursive_circles(new_x, new_y, new_size, levels - 1)


# Начальные параметры
center_x, center_y = 0, 0
initial_size = 2.0
recursion_levels = 3

# Отрисовка рекурсивных окружностей
angles = np.linspace(0, 2 * np.pi, 5, endpoint=False)
for i in range(4):
    angle = i * (2 * np.pi / 4)
    start_x = center_x + initial_size * 4 * np.cos(angle)  # Уменьшаем расстояние между начальными окружностями
    start_y = center_y + initial_size * 4 * np.sin(angle)
    draw_recursive_circles(start_x, start_y, initial_size, recursion_levels)

# Настраиваем график
plt.axis('equal')
plt.show()
