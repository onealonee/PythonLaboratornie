# Открытие файла
with open('Laba7.4.txt', 'r', encoding='utf-8') as myfile:
    # Чтение текста из файла
    text = myfile.read()

# Приведение текста к нижнему регистру для учета разных регистров слова "программа"
lowercase_text = text.lower()

# Разделение текста на слова
words = lowercase_text.split()

# Подсчет количества вхождений слова "программа"
count_programma = words.count("программа")

# Вывод результата
print(f"Слово 'программа' встречается {count_programma} раз(а) в текстовом файле.")
