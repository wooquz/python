# Запрос целого положительного n
n = int(input("Введите целое положительное число n: "))

# Вывод всех числел от 1 до n
print("Числа от 1 до", n, ":")
for i in range(1, n + 1):
    print(i, end=" ")
print()  # перевод строки

# Вывод квадратов чисел от 1 до n
print("Квадраты чисел от 1 до", n, ":")
for i in range(1, n + 1):
    print(f"{i}^2 = {i**2}")

# Вычисление суммы чисел от 1 до n
total = 0
for i in range(1, n + 1):
    total += i

print(f"Сумма чисел от 1 до {n} = {total}")