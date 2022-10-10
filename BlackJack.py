import os
import time
shut_down = "Shutting down"

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
play_game = True
while play_game:

    import random
    print("Welcome to the game of Black Jack")
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

    def random_card(card):
        return card
    my_cards = [random_card(card = random.choice(cards)), random_card(card = random.choice(cards))]
    print(f"Your cards: {my_cards}")
    dealer_card = [random_card(card=random.choice(cards)), random_card(card=random.choice(cards))]
    print(f"Dealer's card: {dealer_card[0]}")
    dealer_new = ["y","n"]
    take_card = True
    take_another = input("Take another card? y/n ")
    if take_another == "y":
        my_cards.append(random_card(card=random.choice(cards)))
        if sum(my_cards) < 21:
            while take_card:
                print(my_cards)
                take_another = input("Take another card? y/n ")
                if take_another == "n":
                    take_card = False
                elif take_another == "y":
                    my_cards.append(random_card(card=random.choice(cards)))
                    if sum(my_cards) > 21 and 11 in my_cards:
                        for i in range(len(my_cards)):
                            if my_cards[i] == 11:
                                my_cards[i] = 1
                    elif sum(my_cards) > 21:
                        take_card = False
                    while (sum(dealer_card) < 15):
                        dealer_card.append(random_card(card=random.choice(cards)))
                    while(sum(dealer_card) > 14 and sum(dealer_card) < 19):
                        if(random.choice(dealer_new) == "y"):
                            dealer_card.append(random_card(card=random.choice(cards)))

            print(my_cards)
            print(dealer_card)
        if sum(my_cards) < 21 and sum(my_cards) > sum(dealer_card):
            print("You win")
        elif (sum(dealer_card) > 21 and sum(my_cards) < 21):
            print("You win")
        elif sum(my_cards) > 21 or sum(my_cards) < sum(dealer_card):
            print("You lose")

        print(my_cards)
        print(dealer_card)
    else:
        while (sum(dealer_card) < 16):
            dealer_card.append(random_card(card=random.choice(cards)))
        while (sum(dealer_card) > 15 and sum(dealer_card) < 19):
            if (random.choice(dealer_new) == "y"):
                dealer_card.append(random_card(card=random.choice(cards)))
        if (sum(my_cards) < 21 and sum(my_cards) > sum(dealer_card)):
            print("You win")
        elif (sum(my_cards) == 21 and sum(dealer_card) != 21):
            print("You win")
        elif (sum(dealer_card) > 21 and sum(my_cards) < 21):
            print("You win")
        elif (sum(my_cards) > 21 or sum(my_cards) < sum(dealer_card)):
            print("You lose")

        print(my_cards)
        print(dealer_card)
    play_again = input("Would you like to play again? y/n ")
    if play_again == "n":
        play_game = False
        cls()
        for i in range(4):

            print(shut_down)
            shut_down += "."
            time.sleep(2)
            cls()


        print("Goodbye")
        time.sleep(2)

    else:
        cls()
