import random
from art import logo, vs
from game_data import data

item = 0
second_item = 0
GAME_OVER = False
count = 0

def game():
    print(logo)
    #Generates a random person out of dicitonary out of list data out of game_data.py
    def generate_random_person():
        global item
        global second_item
        item = random.choice(data)
        second_item = random.choice(data)

    #starts the game. First the code get's the random person out of generate_random_person. Then it tell the player to decide
    def start():
        global item
        global second_item
        generate_random_person()
        while item == second_item:
            second_item = random.choice(data)
        print(f"Compare A: {item['name']}, a {item['description']}, from {item['country']}")
        print(vs)
        print(f"Against B: {second_item['name']}, a {second_item['description']}, from {second_item['country']}")

    def comparison():
        global item
        global second_item
        global GAME_OVER
        exact_followers_A = item['follower_count']
        exact_followers_B = second_item['follower_count']
        global count

        decision = input("Who has more followers on Social Media? Type 'A' or 'B': ")

        if decision == 'A':
            if exact_followers_A > exact_followers_B:
                count += 1
                print(f"That is true, because A has {exact_followers_A} Followers and B has {exact_followers_B} Followers.")
                print(f"Your current count is {count}.")
            else:
                print(f"That is wrong, because B has {exact_followers_B} Followers and A has {exact_followers_A} Followers.")
                print(f"You lost, your final count is {count}")
                GAME_OVER = True

        elif decision == 'B':
            if exact_followers_B > exact_followers_A:
                count += 1
                print(f"That is true, because B has {exact_followers_B} Followers and A has {exact_followers_A} Followers.")
                print(f"Your current count is {count}.")
            else:
                print(f"That is wrong, because B has {exact_followers_B} Followers and A has {exact_followers_A} Followers.")
                print(f"You lost, your final count is {count}")
                GAME_OVER = True
    
    start()
    comparison()

while GAME_OVER != True:
    game()