import random
import time
import json
from datetime import datetime

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()
    
    print("Я загадал число от 1 до 100. Попробуй угадать!")
    
    while True:
        try:
            guess = int(input("Твоя догадка: "))
            attempts += 1
            
            if guess < secret_number:
                print("Слишком мало!")
            elif guess > secret_number:
                print("Слишком много!")
            else:
                end_time = time.time()
                game_time = round(end_time - start_time, 2)
                print(f"Поздравляю! Ты угадал число за {attempts} попыток и {game_time} секунд.")
                return True, attempts, game_time
                
        except ValueError:
            print("Пожалуйста, введите целое число.")

def save_statistics(result, attempts, game_time):
    try:

        with open('statistics.json', 'r') as f:
            stats = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Если файла нет или он пустой, создаем новую статистику
        stats = []
    
    # Добавляем новую запись
    stats.append({
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'result': 'Победа' if result else 'Поражение',
        'attempts': attempts,
        'time_seconds': game_time
    })
    
    # Сохраняем обновленную статистику
    with open('statistics.json', 'w') as f:
        json.dump(stats, f, indent=4)

def show_statistics():
    try:
        with open('statistics.json', 'r') as f:
            stats = json.load(f)
            print("\nСтатистика игр:")
            print("-" * 40)
            for i, game in enumerate(stats, 1):
                print(f"Игра #{i}")
                print(f"Дата: {game['date']}")
                print(f"Результат: {game['result']}")
                print(f"Попыток: {game['attempts']}")
                print(f"Время: {game['time_seconds']} сек")
                print("-" * 40)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Статистика пока недоступна.")

def main():
    print("Добро пожаловать в игру 'Угадай число'!")
    
    while True:
        print("\nМеню:")
        print("1. Начать новую игру")
        print("2. Показать статистику")
        print("3. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            result, attempts, game_time = guess_number()
            save_statistics(result, attempts, game_time)
        elif choice == '2':
            show_statistics()
        elif choice == '3':
            print("Спасибо за игру! До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()