MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

quarter = 0.25
dime = 0.10
nickle = 0.05
penny = 0.01
game_should_continue = True
process_coins_feedback = 'positive'

def print_report():
    for x, y in resources.items():
        print(f"{x}: {y}")

def check_sufficient_resources():
    if selection == "espresso":
        if resources['water'] < 50 or resources['coffee'] < 18:
            print("Sorry, but there are not enough resources in the machine, try it again later.")
            exit()
        else:
            print(f"Water: {resources['water']} Milk: {resources['milk']} Coffee: {resources['coffee']}")
    if selection == "latte":
        if resources['water'] < 200 or resources['milk'] < 150 or resources['coffee'] < 24:
            print("Sorry, but there are not enough resources in the machine, try it again later.")
            exit()
        else:
            print(f"Water: {resources['water']} Milk: {resources['milk']} Coffee: {resources['coffee']}")
    if selection == "cappuccino":
        if resources['water'] < 250 or resources['milk'] < 100 or resources['coffee'] < 24:
            print("Sorry, but there are not enough resources in the machine, try it again later.")
            exit()
        else:
            print(f"Water: {resources['water']} Milk: {resources['milk']} Coffee: {resources['coffee']}")

def lower_resources():
    if selection == "espresso":
        resources['water'] = resources['water'] - int(MENU['espresso']['ingredients']['water'])
        resources['coffee'] = resources['coffee'] - int(MENU['espresso']['ingredients']['coffee'])
    if selection == "latte":
        resources['water'] = resources['water'] - int(MENU['latte']['ingredients']['water'])
        resources['milk'] = resources['milk'] - int(MENU['latte']['ingredients']['milk'])
        resources['coffee'] = resources['coffee'] - int(MENU['latte']['ingredients']['coffee'])
    if selection == "capuccino":
        resources['water'] = resources['water'] - int(MENU['cappuccino']['ingredients']['water'])
        resources['milk'] = resources['milk'] - int(MENU['cappuccino']['ingredients']['milk'])
        resources['coffee'] = resources['coffee'] - int(MENU['cappuccino']['ingredients']['coffee'])

def process_coins():
    global process_coins_feedback
    global game_should_continue
    print("Please insert coins.")
    quarter_q = int(input("How many quarters?: "))
    dimes_q = int(input("How many dimes?: "))
    nickles_q = int(input("How many nickles?: "))
    pennies_q = int(input("How many pennies?: "))
    total_coins = (quarter_q * quarter) + (dimes_q * dime) + (nickles_q * nickle) + (pennies_q * penny)
    if selection == "espresso":
        if total_coins < 1.5:
            print("That is not enough, you will get back your money.")
            game_should_continue = False
            process_coins_feedback = "negative"
        else:
            espresso_cost = MENU['espresso']['cost']
            money_back = total_coins - espresso_cost
            money_back_two_digits = "{:.2f}".format(money_back)
            process_coins_feedback = "positive"
            print(f"Here is ${money_back_two_digits} in change.")
    elif selection == 'latte':
        if total_coins < 2.5:
            print("That is not enough, you will get back your money.")
            game_should_continue = False
            process_coins_feedback = "negative"
        else:
            latte_cost = MENU['latte']['cost']
            money_back_2 = total_coins - latte_cost
            money_back__2_two_digits = "{:.2f}".format(money_back_2)
            process_coins_feedback = "positive"
            print(f"Here is ${money_back__2_two_digits} in change.")
    elif selection == 'cappuccino':
        if total_coins < 3:
            print("That is not enough, you will get back your money.")
            game_should_continue = False
            process_coins_feedback = "negative"
        else:
            cappuccino_cost = MENU['cappuccino']['cost']
            money_back_3 = total_coins - cappuccino_cost
            money_back__3_two_digits = "{:.2f}".format(money_back_3)
            process_coins_feedback = "positive"
            print(f"Here is ${money_back__3_two_digits} in change.")

while game_should_continue:
    selection = input("What would you like? (espresso, latte, cappuccino): ")
    if selection == 'espresso' or selection == 'latte' or selection == 'cappuccino':
        check_sufficient_resources()
        lower_resources()
        process_coins()
        if process_coins_feedback == 'positive':
            print(f"Here is your {selection}")
        else:
            print("Try again!")
    else:
        game_should_continue = False