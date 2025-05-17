# Читание всех строк из data.txt и преобразование в список чисел
with open('/Users/wooquz/Desktop/University/python/lab2/data.txt', 'r') as f:
    numbers = [float(line.strip()) for line in f]

# Вычисление суммы, среднее, максимум и минимум
total = sum(numbers)
average = total / len(numbers) if numbers else 0
maximum = max(numbers) if numbers else None
minimum = min(numbers) if numbers else None

# Записись результов в result.txt
with open('/Users/wooquz/Desktop/University/python/lab2/result.txt', 'w') as f:
    f.write(f"Сумма: {total}\n")
    f.write(f"Среднее: {average}\n")
    f.write(f"Максимум: {maximum}\n")
    f.write(f"Минимум: {minimum}\n")

# Вывод в консоль для наглядности
print("Результаты записаные в result.txt:")
print(f"  Сумма:    {total}")
print(f"  Среднее:  {average}")
print(f"  Максимум: {maximum}")
print(f"  Минимум:  {minimum}")