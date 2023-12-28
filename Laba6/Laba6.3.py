# Ввод размеров двумерного массива от пользователя
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Инициализация двумерного массива
matrix = []
for i in range(rows):
    row = list(map(float, input(f"Введите элементы {i + 1}-й строки через пробел: ").split()))
    matrix.append(row)

# Нахождение суммы элементов каждой строки
sums = []
for row in matrix:
    row_sum = sum(row)
    sums.append(row_sum)

# Вывод результата
for i, row_sum in enumerate(sums):
    print(f"Сумма элементов в {i + 1}-й строке: {row_sum}")
