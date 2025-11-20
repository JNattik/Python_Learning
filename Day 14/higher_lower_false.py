import random
from game_data import data

def start():
    count = 0
    item = random.choice(data)
    second_item = random.choice(data)
    while item == second_item:
        second_item = random.choice(data)
    print(f"Compare A: {item['name']}, a {item['description']}, from {item['country']}")
    print("VS")
    print(f"Against B: {second_item['name']}, a {second_item['description']}, from {second_item['country']}")
    decision = input("Who has more followers on Social Media? Type 'A' or 'B': ")
    specific_count = item['follower_count']
    specific_count2 = second_item['follower_count']
    if decision == 'A':
        if specific_count > specific_count2:
            count += 1
            print(f"Your current count is {count}.")
            start()
        else:
            print(f"That is wrong, because B has {specific_count2} Followers and A has {specific_count} Followers.")
            print(f"You lost, your final count is{count}")
    elif decision == 'B':
        if specific_count2 > specific_count:
            count += 1
            print(f"Your current count is {count}.")
            start()
        else:
            print(f"That is wrong, because B has {specific_count} Followers and A has {specific_count2} Followers.")
            print(f"You lost, your final count is {count}")

start()