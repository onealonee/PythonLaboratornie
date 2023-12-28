# Открытие файла
with open('Laba7.2.txt') as myfile:
    array = [float(i) for i in myfile.read().split()]  # Заполнение списка вещественными числами из файла

# Нахождение суммы положительных элементов
positive_sum = sum(num for num in array if num > 0)

# Вывод результата
print("Сумма положительных элементов:", positive_sum)
