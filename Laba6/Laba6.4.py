# Ввод размеров квадратного массива от пользователя
n = int(input("Введите размер квадратного массива: "))

# Инициализация квадратного массива
matrix = []
for i in range(n):
    row = list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split()))
    matrix.append(row)

# Проверка симметричности относительно главной диагонали
is_symmetric = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break

# Вывод результата
if is_symmetric:
    print("Массив симметричен относительно своей главной диагонали.")
else:
    print("Массив не симметричен относительно своей главной диагонали.")
