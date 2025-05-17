import random

# Генерация списка из 10 случайных целых чисел от 1 до 100
numbers = [random.randint(1, 100) for _ in range(10)]

# Вывод исходного списока
print("Исходный список:", numbers)

# Поиск и вывод максимального и минимального значение
max_value = max(numbers)
min_value = min(numbers)
print("Максимальное значение в списке:", max_value)
print("Минимальное значение в списке:", min_value)

# Вычисление и вывод суммы всех элементов
total_sum = sum(numbers)
print("Сумма всех элементов списка:", total_sum)

# Сортировка списока по возрастанию и выводим его
numbers.sort()
print("Список после сортировки по возрастанию:", numbers)