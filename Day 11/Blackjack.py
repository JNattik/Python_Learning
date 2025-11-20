#Ground rules: If player or dealer has value 21 with his cards they have blackjack and win. If either has a value over 21 they loose directly
#1. Dealer gets one card and player 2 Cards --> Random Cards from the list
#2. Option 1: Draw another Card or Decline --> Decline --> Game is over and Dealer starts playing and gets another card --> If value is below 17 --> he has to draw another card --> if total value is higher than players total value, Dealer wins, otherwise player wins
#3. Option 2: Draw another Card or Decline...
#4. Options continue until player has 21, over 21 or he Declines to take another card
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
Game_Start = input("Welcome to Blackjack. Would you like to play a game of Blackjack? Type 'yes' or 'no' ")

player_cards = []
dealer_cards = []

if Game_Start == "yes":
    random_card1 = random.choice(cards)
    random_card2 = random.choice(cards)
    player_cards.append(random_card1)
    player_cards.append(random_card2)
    random_card3 = random.choice(cards)
    dealer_cards.append(random_card3)
    print(player_cards)
    print(dealer_cards)

    x = sum(player_cards)
    y = sum(dealer_cards)

    while x < 21 or Option_1 == "Decline":
        Option_1 = input("Draw another Card from the deck or Decline? Type 'y' or 'n' ")
        if Option_1 == "y":
            x += random.choice(cards)
            for z in player_cards:
                if z == 11 and x > 21:
                    z = 1
            print(player_cards)
            if x == 21:
                print("Blackjack, You won!")
                exit()
        elif Option_1 == "n":
            while y < 17:
                y += random.choice(cards)
                print(dealer_cards )
                if x < 22 and x> y:
                    print("You win!")
                    exit()
                elif x == y:
                    print("It´s a Draw!")
                    exit()
                elif x < y and y < 22:
                    print("You lost, better luck next time!")
                    exit()

    if x > 21:
        print("You lost!")
                
else:
    print("Okay, bye")

