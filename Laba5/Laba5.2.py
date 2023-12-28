import math

def g(u, t):
    if u - t < -2:
        return (u + t)**2
    elif -2 <= u - t < 5:
        return u / (t**2 + 1)
    elif u - t >= 5:
        return u - t

def f(x, y):
    numerator = g(x, y) + g(abs(x - y), x + y)
    denominator = 2 * g(math.sqrt(x), math.sqrt(y)) + 2

    if denominator != 0:
        return numerator / denominator
    else:
        raise ValueError("Знаменатель равен нулю. Деление на ноль невозможно.")

# Вычисление значений функции f(x, y) для нескольких значений аргументов
try:
    x_values = [1, 3, 5]
    y_values = [2, 4, 6]

    for x, y in zip(x_values, y_values):
        result = f(x, y)
        print(f"f({x}, {y}) = {result}")

except ValueError as e:
    print(f"Ошибка: {e}")
