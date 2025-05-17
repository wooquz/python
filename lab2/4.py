import re

# Читение текста из text.txt
with open('/Users/wooquz/Desktop/University/python/lab2/text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Шаблоны
email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
phone_pattern = r'\+7-\d{3}-\d{3}-\d{2}-\d{2}'
capital_word_pattern = r'\b[А-ЯA-Z][а-яa-zA-Z]*\b'

# Поиск всего
emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)
capital_words = re.findall(capital_word_pattern, text)

# Сохранение результатов
with open('/Users/wooquz/Desktop/University/python/lab2/emails.txt', 'w', encoding='utf-8') as f:
    for e in sorted(set(emails)):
        f.write(e + '\n')

with open('/Users/wooquz/Desktop/University/python/lab2/phones.txt', 'w', encoding='utf-8') as f:
    for p in sorted(set(phones)):
        f.write(p + '\n')

with open('/Users/wooquz/Desktop/University/python/lab2/capital_words.txt', 'w', encoding='utf-8') as f:
    for w in sorted(set(capital_words)):
        f.write(w + '\n')

# Вывод в консоль
print("Найдено email-адресов:", len(emails))
print("Найдено телефонов:", len(phones))
print("Найдено слов с заглавной буквы:", len(capital_words))