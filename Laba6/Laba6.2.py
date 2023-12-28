# Ввод данных от пользователя
input_str = input("Введите элементы массива через пробел: ")
array = [float(element) for element in input_str.split()]

# Изменение порядка значений на обратный
array.reverse()

# Вывод результата без точки после целой части и без скобок
result_str = ", ".join(map(lambda x: str(int(x)), array))
print(f"Массив после изменения порядка значений на обратный: {result_str}")
