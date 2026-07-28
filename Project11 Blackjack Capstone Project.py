import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "You both draw with equal scores."
    elif c_score == 0:
        return "You lose the game as the Dealer have a BlackJack."
    elif u_score == 0:
        return "You won the game as you have a BlackJack."
    elif u_score > 21:
        return "You lose the game as you are over 21."
    elif c_score > 21:
        return "You won the game as the Dealer is over 21."
    elif u_score > c_score:
        return f"You won the game with highest score of {u_score}."
    else:
        return f"You lose the game as the Dealer has highest score of {c_score}."


def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for thing in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are : {user_cards}", f"  Your current score is: {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = input("Do you want to draw another card? Type 'y' to draw or 'n' to pass: ").lower()
            if draw_card == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play the game of BlackJack? Type 'y' to restart or type 'n' to pass: ") == "y":
    print("\n" * 20)
    play_game()
