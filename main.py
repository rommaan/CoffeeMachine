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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

order = ""
payment = 0.00
balance = 0.00
enough_stuff = True
enough_money = True
change = 0.00
working = True


def check_resources(order, enough_stuff):
    drink = order
    drink_ingredient = ""
    drink_ingredient_quantity = 0
    for drink_ingredient in MENU[drink]["ingredients"]:
        drink_ingredient_quantity = MENU[drink]["ingredients"][drink_ingredient]
        if drink_ingredient_quantity > RESOURCES[drink_ingredient]:
            print(f"Sorry! There is not enough {drink_ingredient}.")
            enough_stuff = False
        else:
            RESOURCES[drink_ingredient] -= drink_ingredient_quantity
            # print(f"Will use {drink_ingredient_quantity} of {drink_ingredient}")
            enough_stuff = True
    return drink_ingredient, drink_ingredient_quantity, enough_stuff, RESOURCES


def accept_coins():
    print("Please insert coins!")
    quarters = float(input("How many quarters:  ")) * 0.25
    # print(f"inserted ${quarters} in quarters")
    dimes = float(input("How many dimes:  ")) * 0.10
    # print(f"inserted ${dimes} in dimes")
    nickles = float(input("How many nickles:  ")) * 0.05
    # print(f"inserted ${nickles} in nickles")
    pennies = float(input("How many pennies:  ")) * 0.01
    # print(f"inserted ${pennies} in pennies")
    payment = round(float(quarters + dimes + nickles + pennies), 2)
    print(f"You inserted ${payment}.")
    return payment


def check_payment(order, payment, change, balance, enough_money):
    if payment < MENU[order]["cost"]:
        enough_money = False
    else:
        balance += MENU[order]["cost"]
        enough_money = True
        change = round((payment - MENU[order]["cost"]), 2)
    return payment, change, balance, enough_money

def recalculate_resources(order):
    if order == "espresso":
        RESOURCES["water"] -= MENU["espresso"]["ingredients"]["water"]
        # print(f"Water: {RESOURCES['water']}")
        RESOURCES["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        # print(f"Coffee: {RESOURCES['coffee']}")
    elif order == "latte":
        RESOURCES["water"] -= MENU["latte"]["ingredients"]["water"]
        # print(f"Water: {RESOURCES['water']}")
        RESOURCES["milk"] -= MENU["latte"]["ingredients"]["milk"]
        # print(f"Milk: {RESOURCES['milk']}")
        RESOURCES["coffee"] -= MENU["latte"]["ingredients"]["milk"]
        # print(f"Coffee: {RESOURCES['coffee']}")
    elif order == "cappuccino":
        RESOURCES["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        # print(f"Water: {RESOURCES['water']}")
        RESOURCES["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        # print(f"Milk: {RESOURCES['milk']}")
        RESOURCES["coffee"] -= MENU["cappuccino"]["ingredients"]["milk"]
        # print(f"Coffee: {RESOURCES['coffee']}")
    else:
        print("No such drink")
    return RESOURCES


def recalculate_balance(order, balance):
    balance_addition = 0.00
    for choice, value in MENU.items():
        if order == value:
            balance_addition = MENU[choice]["cost"]
            balance += balance_addition
            print(f"Balance : {balance}")
            return balance


def report():
    print(f"Your new balance is ${balance}")
    print(f"Water: {RESOURCES['water']}")
    print(f"Milk: {RESOURCES['milk']}")
    print(f"Coffee: {RESOURCES['coffee']}")


while working:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order in MENU.keys():
        print("Ein moment!")
        print(f"{order} was ordered")
        print(f"Price is ${MENU[order]['cost']}")
        check_resources(order, enough_stuff)
        if enough_stuff:
            payment = accept_coins()
            # print(f"{payment} in coins was accepted")
            if payment >= MENU[order]["cost"]:
                enough_money = True
                balance += MENU[order]["cost"]
                change = round((payment - MENU[order]["cost"]), 2)
                print(f"Here is ${change} dollars in change.")
                print(f"Here is your {order}.Enjoy!")
                recalculate_balance(order, balance)
                # print(f"Your order is {order}. Balance is {balance}")
            else:
                enough_money = False
                print(f"Sorry {payment} is not enough. Money refunded.")
        else:
            print(f"Sorry! There is not enough resources.")
    elif order == "report":
        print("Report was ordered")
        report()
    elif order == "off":
        working = False
        print("Machine is turning off")
    else:
        print("Sorry we don't have this on the menu")

