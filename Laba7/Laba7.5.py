def backup_original_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as myfile:
        original_text = myfile.read()
    return original_text

def replace_lowercase_with_uppercase(file_path):
    # Создаем резервную копию оригинального текста
    original_text = backup_original_text(file_path)

    # Открываем файл и читаем текст
    with open(file_path, 'r', encoding='utf-8') as myfile:
        text = myfile.read()

    # Замена строчных букв русского алфавита на заглавные
    modified_text = text.upper()

    # Запись измененного текста обратно в файл
    with open(file_path, 'w', encoding='utf-8') as myfile:
        myfile.write(modified_text)

    print("Замена на заглавные буквы успешно выполнена.")

    # Возвращаем резервную копию для возможности восстановления исходного текста
    return original_text

def replace_uppercase_with_lowercase_and_capitalize(file_path):
    # Создаем резервную копию оригинального текста
    original_text = backup_original_text(file_path)

    # Открываем файл и читаем текст
    with open(file_path, 'r', encoding='utf-8') as myfile:
        text = myfile.read()

    # Замена строчных букв русского алфавита на строчные
    modified_text = text.lower()

    # Капитализация первой буквы каждого предложения
    modified_text = '. '.join(sentence.capitalize() for sentence in modified_text.split('. '))

    # Запись измененного текста обратно в файл
    with open(file_path, 'w', encoding='utf-8') as myfile:
        myfile.write(modified_text)

    print("Замена на строчные буквы и капитализация успешно выполнены.")

    # Возвращаем резервную копию для возможности восстановления исходного текста
    return original_text

# Пример использования
file_path = 'Laba7.5.txt'  # Замените на фактическое имя вашего текстового файла

# Пользовательский выбор
choice = input("Введите 1, чтобы заменить на заглавные буквы, или 2, чтобы заменить на строчные буквы и капитализировать: ")

if choice == '1':
    # Замена на заглавные буквы
    replace_lowercase_with_uppercase(file_path)
elif choice == '2':
    # Замена на строчные буквы и капитализация
    replace_uppercase_with_lowercase_and_capitalize(file_path)
else:
    print("Некорректный ввод. Пожалуйста, введите 1 или 2.")
