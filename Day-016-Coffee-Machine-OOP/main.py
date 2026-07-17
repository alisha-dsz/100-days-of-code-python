import coffee_maker
import menu
import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

should_order = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while should_order:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        print("The coffee machine has been turned off. Thank you.")
        should_order = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
