# Программа с заполнением матрицы в ручную
import numpy as np

# Задание размерности и данных матрицы в коде программы
matrix_data = [
    [1, 1, 3],
    [4, 4, 1],
    [7, 8, 2]
]

# Преобразование списка списков в NumPy-массив
matrix = np.array(matrix_data)

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
