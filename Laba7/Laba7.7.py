def read_matrix(file_path):
    """Считывает матрицу из файла."""
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = [int(num) for num in line.split()]  # Изменено на целые числа
            matrix.append(row)
    return matrix

def multiply_matrices(matrix1, matrix2):
    """Умножает две матрицы."""
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(element)
        result_matrix.append(row)
    return result_matrix

# Пример использования
file_path_matrix1 = 'Laba7.7.matrix1.txt'  # Замените на фактическое имя файла с первой матрицей
file_path_matrix2 = 'Laba7.7.matrix2.txt'  # Замените на фактическое имя файла со второй матрицей

# Считываем матрицы из файлов
matrix1 = read_matrix(file_path_matrix1)
matrix2 = read_matrix(file_path_matrix2)

# Проверяем, что матрицы можно умножить
if len(matrix1[0]) != len(matrix2):
    print("Умножение невозможно. Количество столбцов первой матрицы не равно количеству строк второй матрицы.")
else:
    # Умножаем матрицы
    result_matrix = multiply_matrices(matrix1, matrix2)

    # Выводим результат в терминал
    print("Результат умножения матриц:")
    for row in result_matrix:
        print(' '.join(map(str, row)))
