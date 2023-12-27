import math

# Пользовательская функция для вычисления арксинуса
def arcsin(a):
    if -1 <= a <= 1:
        return math.degrees(math.atan(a / math.sqrt(1 - a**2)))
    else:
        raise ValueError("Значение a должно находиться в интервале [-1, 1]")

# Пользовательская функция для вычисления арккосинуса
def arccos(a):
    if -1 <= a <= 1:
        return math.degrees(math.atan(math.sqrt(1 - a**2) / a))
    else:
        raise ValueError("Значение a должно находиться в интервале [-1, 1]")

# Пользовательская функция для вычисления арккотангенса
def arcctg(a):
    if a != 0:
        return math.degrees(math.atan(1 / a))
    else:
        raise ValueError("Значение a не может быть равным 0")

# Пользовательская функция для перевода радианной меры угла в градусную
def rad_to_deg(radians):
    return math.degrees(radians)

# Значение a (при a > 0)
a = float(input("Введите значение a (a > 0): "))

try:
    # Вычисление значений с использованием пользовательских функций
    result_arcsin = arcsin(a)
    result_arccos = arccos(a)
    result_arcctg = arcctg(a)

    # Вычисление значений с использованием стандартных функций
    result_arcsin_standard = math.degrees(math.asin(a))
    result_arccos_standard = math.degrees(math.acos(a))
    result_arcctg_standard = math.degrees(math.atan(1 / a))

    # Вывод результатов
    print(f"Значение arcsin({a}) с пользовательской функцией: {result_arcsin}")
    print(f"Значение arcsin({a}) со стандартной функцией: {result_arcsin_standard}")
    print()
    print(f"Значение arccos({a}) с пользовательской функцией: {result_arccos}")
    print(f"Значение arccos({a}) со стандартной функцией: {result_arccos_standard}")
    print()
    print(f"Значение arcctg({a}) с пользовательской функцией: {result_arcctg}")
    print(f"Значение arcctg({a}) со стандартной функцией: {result_arcctg_standard}")
except ValueError as e:
    print(f"Ошибка: {e}")
