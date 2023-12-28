def find_max_index(array):
    if not array:
        raise ValueError("Массив не должен быть пустым")

    max_value = array[0]
    max_indices = [0]

    for i in range(1, len(array)):
        if array[i] > max_value:
            max_value = array[i]
            max_indices = [i]
        elif array[i] == max_value:
            max_indices.append(i)

    return max_indices, max_value

# Пример использования
try:
    # Ввод данных от пользователя
    input_str = input("Введите элементы массива через пробел: ")
    array = [float(element) for element in input_str.split()]

    # Находим индексы наибольших элементов
    max_indices, max_value = find_max_index(array)

    # Вывод результата
    if len(max_indices) == 1:
        print(f"Наибольший элемент {int(max_value)} в массиве находится в позиции {max_indices[0]}.")
    else:
        max_value_str = int(max_value) if max_value.is_integer() else max_value
        print(f"Несколько наибольших элементов {max_value_str} находятся в позициях: {', '.join(map(str, max_indices))}.")

except ValueError as e:
    print(f"Ошибка: {e}. Убедитесь, что введены корректные числа.")
