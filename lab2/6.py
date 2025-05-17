import re
from datetime import datetime

# Четние текста
with open('/Users/wooquz/Desktop/University/python/lab2/text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Поиск даты в формате DD.MM.YYYY
date_pattern = r'\b(\d{2})\.(\d{2})\.(\d{4})\b'
found = re.findall(date_pattern, text)

# Преобразование и сбор в список строк YYYY-MM-DD
dates = []
for day, month, year in found:
    try:
        dt = datetime.strptime(f"{day}.{month}.{year}", "%d.%m.%Y")
        dates.append(dt.strftime("%Y-%m-%d"))
    except ValueError:
        pass  # Пропуск некорректных дат

# Сортировка по возрастанию
dates_sorted = sorted(set(dates))

# Сохранение в файл
with open('/Users/wooquz/Desktop/University/python/lab2/dates.txt', 'w', encoding='utf-8') as f:
    for d in dates_sorted:
        f.write(d + '\n')

# Вывод результата
print("Найденные и преобразованные даты:")
for d in dates_sorted:
    print(" ", d)