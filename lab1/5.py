import random  # для генерации случайных чисел

def main():
    # Генерирация списока из 20 случайных чисел от 1 до 100
    numbers = [random.randint(1, 100) for _ in range(20)]
    print("Сгенерированный список:", numbers)

    # Отбор всех чётных числел из списка
    even_numbers = [num for num in numbers if num % 2 == 0]
    print("Чётные числа:", even_numbers)

    # Отбор всех числел, которые делятся на 3
    divisible_by_three = [num for num in numbers if num % 3 == 0]
    print("Числа, делящиеся на 3:", divisible_by_three)

    # Вычисление среднего арифметического всех чисел в списке
    if numbers:
        average = sum(numbers) / len(numbers)
    else:
        average = 0  # на случай пустого списка, хотя здесь это не случится
    print("Среднее арифметическое:", average)

if __name__ == "__main__":
    main()
