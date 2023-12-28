def count_word_occurrences(file_path):
    # Открытие файла и чтение текста
    with open(file_path, 'r', encoding='utf-8') as myfile:
        text = myfile.read()

    # Разделение текста на слова, учитывая один или несколько пробелов
    words = text.split()

    # Создание словаря для хранения частоты встречаемости слов
    word_occurrences = {}

    # Подсчет частоты встречаемости каждого слова
    for word in words:
        # Приведение слова к нижнему регистру для учета регистра
        normalized_word = word.lower()

        # Обновление словаря частоты встречаемости слов
        word_occurrences[normalized_word] = word_occurrences.get(normalized_word, 0) + 1

    return word_occurrences

# Пример использования
file_path = 'Laba7.6.txt'  # Замените на фактическое имя вашего текстового файла

# Получение словаря частоты встречаемости слов
word_occurrences = count_word_occurrences(file_path)

# Вывод результатов
for word, occurrences in word_occurrences.items():
    print(f'Слово "{word}" встречается {occurrences} раз(а).')
