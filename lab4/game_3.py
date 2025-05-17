 # разметка
def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")

def check_winner(board):
    # по горизонтали
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    
    # gj dthnbrfkb
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    
    # по диагонали
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    
    


    if " " not in board:
        return "Ничья"
    
    return None

def make_move(board, player):
    while True:
        try:
            position = int(input(f"Игрок {player}, введите номер клетки (1-9): ")) - 1
            if 0 <= position <= 8 and board[position] == " ":
                board[position] = player
                return
            else:
                print("Неверный ход. Попробуйте ещё раз.")
        except ValueError:
            print("Пожалуйста, введите число от 1 до 9.")

def game():
    board = [" "] * 9
    current_player = "X"
    
    print("Добро пожаловать в Крестики-нолики!")
    print("Номера клеток:")
    print_board(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    print("\nНачинаем игру!\n")
    
    while True:
        print_board(board)
        make_move(board, current_player)
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "Ничья":
                print("Ничья!")
            else:
                print(f"Игрок {winner} победил!")
            break
        
        # Смена игрока
        current_player = "O" if current_player == "X" else "X"

def main():
    while True:
        game()
        play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
        if play_again != "да":
            print("Спасибо за игру! До свидания!")
            break

if __name__ == "__main__":
    main()