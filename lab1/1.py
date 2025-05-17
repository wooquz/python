# Запрос трех числел и преобрование их в float
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

# Поиск наибольшее и наименьшее
max_value = max(a, b, c)
min_value = min(a, b, c)

# Проверка, все ли числа равны
all_equal = (a == b == c)

# Вывод результатов
print(f"Наибольшее число: {max_value}")
print(f"Наименьшее число: {min_value}")
print("Все числа равны." if all_equal else "Не все числа равны.")