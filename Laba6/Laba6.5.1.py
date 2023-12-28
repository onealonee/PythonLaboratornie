# Программа с автозаполнением через модуль рандом
import numpy as np

# Ввод размерности матрицы от пользователя
n = int(input("Введите размерность квадратной матрицы: "))

# Генерация псевдослучайных элементов матрицы
matrix = np.random.rand(n, n)

# Вывод исходной матрицы
print("Исходная матрица:")
print(matrix)

# Нахождение обратной матрицы
try:
    inverse_matrix = np.linalg.inv(matrix)

    # Вывод обратной матрицы
    print("\nОбратная матрица:")
    print(inverse_matrix)

except np.linalg.LinAlgError:
    print("\nОбратной матрицы не существует.")
