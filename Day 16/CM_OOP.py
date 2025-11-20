from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu_1 = Menu()
coffe_maker_1 = CoffeeMaker()
money_machine_1 = MoneyMachine()


while is_on:
    options = menu_1.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker_1.report()
        money_machine_1.report()
    else:
        drink = menu_1.find_drink(choice)
        if coffe_maker_1.is_resource_sufficient(drink):
            if money_machine_1.make_payment(drink.cost):
                coffe_maker_1.make_coffee(drink)