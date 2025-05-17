# Запрос целого неотрицательного n
n = int(input("Введите неотрицательное целое число n: "))

# Вывод числа от n до 1
print(f"Числа от {n} до 1:")
current = n
while current >= 1:
    print(current, end=" ")
    current -= 1
print()  # перевод строки

# Вычисление факториала n (n!)
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

print(f"Факториал числа {n} = {factorial}")