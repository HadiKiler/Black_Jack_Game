import random
from art import logo
from replit import clear

def get_random_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return cards[random.randint(0, len(cards)-1)]


def game():
    print(logo)
    my_cards = []
    computer_cards = []

    def print_cards():
        print(f"""
        computer_card = {computer_cards}
        your_cards = {my_cards}
            """)
        
    my_cards.append(get_random_card())  
    my_cards.append(get_random_card())
    computer_cards.append(get_random_card())  
    computer_cards.append(get_random_card())  
    hit = True
    
    if sum(my_cards) == 21 or sum(computer_cards) == 21:
        print_cards()
        if sum(my_cards) == sum(computer_cards):
            print('draw 🤔')
        elif sum(my_cards) == 21:
            print("You Have a Black Jack 😎")
        elif sum(computer_cards) == 21:    
            print("Computer Have a Black Jack 😭")
        return
    
    while hit:
        print(f"""
        computer_card = {computer_cards[0]}
        your_cards = {my_cards}
        """)
        if sum(my_cards)>=21:
            break
        result = input('do need another card? (y/n) : ')
        if result.lower() == "y":
            my_cards.append(get_random_card())
            continue     
        break
    
    while sum(computer_cards) < 17:
        computer_cards.append(get_random_card())

    print_cards()
    if sum(my_cards) == sum(computer_cards):
        print('draw 🤔')
    elif sum(computer_cards)>21:
        print("you win 😎")
    elif sum(my_cards)>21:    
        print("you lose 😭")
    elif sum(my_cards) > sum(computer_cards):
        print('you win 😎')
    else:
        print('you lose 😭')
    clear()


while True:
    game()
    next = input('------------- do you want to play again? (y/n) : ')
    if next == "n":
        break