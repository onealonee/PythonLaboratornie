def geometric_progression(a, r, n):
    """
    Функция для вычисления n первых членов геометрической прогрессии.

    :param a: Первый член прогрессии.
    :param r: Знаменатель прогрессии.
    :param n: Количество членов прогрессии.
    :return: Список n членов геометрической прогрессии.
    """
    progression = [a * (r ** i) for i in range(n)]
    return progression

def sum_of_geometric_progression(a, r, n, m):
    """
    Функция для вычисления суммы всех членов геометрической прогрессии с номерами от n до m.

    :param a: Первый член прогрессии.
    :param r: Знаменатель прогрессии.
    :param n: Номер начального члена прогрессии.
    :param m: Номер конечного члена прогрессии.
    :return: Сумма членов геометрической прогрессии от n до m.
    """
    if n >= m:
        raise ValueError("Некорректные значения n и m. Убедитесь, что n < m.")

    progression = geometric_progression(a, r, m + 1)  # Создаем прогрессию до m
    sum_of_progression = sum(progression[n:m + 1])  # Считаем сумму членов от n до m
    return sum_of_progression

# Ввод данных от пользователя
a = float(input("Введите первый член геометрической прогрессии (a): "))
r = float(input("Введите знаменатель геометрической прогрессии (r): "))
n = int(input("Введите номер начального члена прогрессии (n): "))
m = int(input("Введите номер конечного члена прогрессии (m): "))

try:
    # Проверка n > m
    if n > m:
        raise ValueError("Некорректные значения n и m. Убедитесь, что n < m.")

    # Вычисление суммы членов геометрической прогрессии от n до m
    result = sum_of_geometric_progression(a, r, n, m)
    print(f"Сумма членов геометрической прогрессии от {n} до {m}: {result}")

except ValueError as e:
    print(f"Ошибка: {e}")
