# Создание списка от 1 до 20
numbers = list(range(1, 21))

# Фильтрация: оставление только чётные
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Увеличение каждое на 10
plus_ten = list(map(lambda x: x + 10, evens))

# Сортировка по убыванию
sorted_desc = sorted(plus_ten, reverse=True)

# Вывод
print("Исходные чётные числа:", evens)
print("После прибавления 10:", plus_ten)
print("Отсортировано по убыванию:", sorted_desc)