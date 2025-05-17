import game_1
import game_2
import game_3
def main():
    print("Игры")
    print('1.Угадай число')
    print('2.Блэк Джэк')
    print('3.Крестики нолики')
    print('0.Выход')

    Выбор = input("Выбери игру: ")
    if Выбор == "1":
        game_1.play_game()
    elif Выбор == "2":
        game_2.play_game()
    elif Выбор == "3":
        game_3.play_game()
    elif Выбор == "0":
        print("Выход")
    else:
        print('Неверный ввод')
if __name__ == "__main__":
    main()