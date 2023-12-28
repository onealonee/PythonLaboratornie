# Открытие файла
with open('Laba7.3.txt') as myfile:
    # Чтение строк из файла и преобразование в числа
    rows = [list(map(float, line.split())) for line in myfile]

# Нахождение среднего арифметического сумм элементов строк
average_sums = [sum(row) / len(row) for row in rows]

# Вывод результатов
print("Средние арифметические сумм элементов строк:")
for i, average_sum in enumerate(average_sums, start=1):
    print(f"Строка {i}: {average_sum}")
