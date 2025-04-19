import random


#Рандом карта от 2 до 11
def deal_card():
    return random.randint(2, 11)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    return sum(cards)

def winner(player_score, dealer_score):
    if player_score == dealer_score:
        return "Ничья!"
    elif dealer_score == 0:
        return "Дилер выиграл с Blackjack!"
    elif player_score == 0:
        return "Игрок выиграл с Blackjack!"
    elif player_score > 21:
        return "Перебор! Дилер выиграл."
    elif dealer_score > 21:
        return "Дилер перебрал! Игрок выиграл."
    elif player_score > dealer_score:
        return "Игрок выиграл!"
    else:
        return "Дилер выиграл!"

def play_game():
    player_cards = []
    dealer_cards = []
    is_game_over = False

    #первые карты
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        
        print(f"Карты игрока: {player_cards}, сумма: {player_score}")
        print(f"Первая карта дилера: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            #игрок
            player_choice = input("Взять карту? (+/-): ").lower()
            if player_choice == "+":
                player_cards.append(deal_card())
            else:
                is_game_over = True

    #дилер
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Карты игрока: {player_cards}, сумма: {player_score}")
    print(f"Карты дилера: {dealer_cards}, сумма: {dealer_score}")
    print(winner(player_score, dealer_score))

def main():
    print("Добро пожаловать в игру '21 очко'!")
    while True:
        play_game()
        again = input("Сыграем ещё раз? (да/нет): ").lower()
        if again != "да":
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()