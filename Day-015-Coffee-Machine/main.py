MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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


def after_order(menu, item, resource):
    if item:
        resource["water"]-=menu[item]["ingredients"]["water"]
        resource["milk"] -= menu[item]["ingredients"]["milk"]
        resource["coffee"] -= menu[item]["ingredients"]["coffee"]
        return resource["water"], resource["milk"], resource["coffee"]

def check_resource(menu, item, resource):
    for resource_item in resource:
        if resource[resource_item] < menu[item]['ingredients'][resource_item]:
            return f"Sorry there's no enough {resource_item}."

should_game_continue = True
money = 0

while should_game_continue:
    updated_resource = resources
    order = input("What would you like? ")

    if order in ['latte', 'espresso', 'cappuccino']:
        check = check_resource(MENU, order, updated_resource)
        if check:
            print(check)
        else:
            after_order(MENU,order, updated_resource)
            print("Please insert the coins.")
            quarter = float(input("How many quarters? "))
            dime = float(input("How many dimes? "))
            nickle = float(input("How many nickles? "))
            penny = float(input("How many pennies? "))
            calculated_amount = (0.25 * quarter) + (0.10 * dime) + (0.05 * nickle) + (0.01 * penny)

            if calculated_amount < MENU[order]['cost']:
                print("Sorry the amount is not enough. Money has been refunded.")
            elif calculated_amount > MENU[order]['cost']:
                money += calculated_amount
                change = calculated_amount - MENU[order]['cost']
                money -= change
                print(f"Here's the change ${round(change, 2)}")
                print(f"Here's your {order}. Enjoy!")
            else:
                money += calculated_amount
                print(f"Here's your {order}. Enjoy!")

    if order == 'report':
        print(f"Water : {updated_resource["water"]}ml\n"
              f"Milk : {updated_resource["milk"]}ml\n"
              f"Coffee : {updated_resource["coffee"]}g\n"
              f"Money : ${money}")

    if order == 'off':
        print("The coffee machine has been turned off.")
        should_game_continue = False

