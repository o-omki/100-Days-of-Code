from os import system, name
import random
import game_logo

def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def deal_cards():
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_list)

def calculate_cost(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_scores(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You went over. You lost."
    if player_score == computer_score:
        return "Draw!"
    elif player_score == 0:
        return "You win with a Blackjack!"
    elif computer_score == 0:
        return "You lost, opponent has Blackjack."
    elif player_score > 21:    
        return "You went over. You lost."
    elif computer_score > 21:
        return "You won! The computer went over."
    elif player_score > computer_score:
        return "You won!"
    else:
        return "You lost."

def initialise_game():
    print(game_logo.logo)
    
    player_hand = []
    computer_hand = []
    game_end = False

    for _ in range(2):
        player_hand.append(deal_cards())
        computer_hand.append(deal_cards())

    while not game_end:
        player_score = calculate_cost(player_hand)
        computer_score = calculate_cost(computer_hand)
        print(f"    Your cards: {player_hand}, current score: {player_score}")
        print(f"    Opponent's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_end = True
        
        else:
            draw_card = input("Enter 'y' to draw another card, or 'n' to pass: ")
            if draw_card.lower() == 'y':
                player_hand.append(deal_cards())
            else:
                game_end = True 
        
    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_cards())
        computer_score = calculate_cost(computer_hand)
    
    print(f"    Your final hand: {player_hand}, final score: {player_score}")
    print(f"    Opponent's final hand: {computer_hand}, final score: {computer_score}")
    print(compare_scores(player_score, computer_score))

while input("\nStart a Blackjack game? (y / n): ") == 'y':
    clear_screen()
    initialise_game()
