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
    drink_ingredient_name = ""
    drink_ingredient_quantity = 0
    for drink_ingredient in drink:
        if drink in MENU:
            print(f"order ingredient is: {drink_ingredient_name} = {drink_ingredient_quantity}")
            return drink_ingredient_name, drink_ingredient_quantity
        else:
            print("Sorry we don't have this on the menu")
    resource_ingredient_name = ""
    resource_ingredient_quantity = 0
    for resource_ingredient in RESOURCES:
        if drink_ingredient_name == resource_ingredient_name:
            if drink_ingredient_quantity > resource_ingredient_quantity:
                print(f"Sorry! There is not enough {resource_ingredient_name}.")
                enough_stuff = False
            else:
                enough_stuff = True
    return enough_stuff


def accept_coins(order):
    print("Please insert coins!")
    quarters = int(input("How many quarters:  ")) * 0.25
    dimes = int(input("How many dimes:  ")) * 0.10
    nickles = int(input("How many nickles:  ")) * 0.05
    pennies = int(input("How many pennies:  ")) * 0.01
    payment = quarters + dimes + nickles + pennies
    print(f"You inserted ${payment}.")
    return payment


def check_payment(order, payment, balance):
    change = 0.0
    enough_money = True
    if order == "espresso":
        if payment < MENU["espresso"]["cost"]:
            enough_money = False
        else:
            balance += MENU["espresso"]["cost"]
            enough_money = True
            change = round((payment - MENU["espresso"]["cost"]), 2)
    elif order == "latte":
        if payment < MENU["latte"]["cost"]:
            enough_money = False
        else:
            balance += MENU["latte"]["cost"]
            enough_money = True
            change = round((payment - MENU["latte"]["cost"]), 2)
    elif order == "cappuccino":
        if payment < MENU["cappuccino"]["cost"]:
            enough_money = False
        else:
            balance += MENU["cappuccino"]["cost"]
            enough_money = True
            change = round((payment - MENU["cappuccino"]["cost"]), 2)
    else:
        print(f"no such drink as {order} exists")
    return enough_money, order, change, balance


def recalculate_resources(order):

    if order == "espresso":
        RESOURCES["water"] -= MENU["espresso"]["ingredients"]["water"]
        print(f"Water: {RESOURCES['water']}")
        RESOURCES["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        print(f"Coffee: {RESOURCES['coffee']}")
    elif order == "latte":
        RESOURCES["water"] -= MENU["latte"]["ingredients"]["water"]
        print(f"Water: {RESOURCES['water']}")
        RESOURCES["milk"] -= MENU["latte"]["ingredients"]["milk"]
        print(f"Milk: {RESOURCES['milk']}")
        RESOURCES["coffee"] -= MENU["latte"]["ingredients"]["milk"]
        print(f"Coffee: {RESOURCES['coffee']}")
    elif order == "cappuccino":
        RESOURCES["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        print(f"Water: {RESOURCES['water']}")
        RESOURCES["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        print(f"Milk: {RESOURCES['milk']}")
        RESOURCES["coffee"] -= MENU["cappuccino"]["ingredients"]["milk"]
        print(f"Coffee: {RESOURCES['coffee']}")
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
    return "no such drink in the machine"


def report():
    print(f"Your new balance is ${balance}")
    print(f"Water: {RESOURCES['water']}")
    print(f"Milk: {RESOURCES['milk']}")
    print(f"Coffee: {RESOURCES['coffee']}")


while working:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        working = False
    elif order == "report":
        report()
    else:
        check_resources(order, enough_stuff)
        if enough_stuff:
            accept_coins(order)
            check_payment(order, payment, balance)
            if enough_money:
                print(f"Here is ${change} dollars in change.")
                print(f"Here is your {order}.Enjoy!")
                recalculate_balance(order, balance)
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry! There is not enough resources.")












# TODO 5. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
# Prompt user by asking “What would you like? (espresso/latte/cappuccino):”


# TODO 6. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# TODO 7. Turn off the Coffee Machine by entering “off” to the prompt.
# For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.



















def select_drink(drink):
    drink = ORDER
    for choice, value in MENU.items():
        if drink == value:
            choice = MENU[drink]
            print(f"drink: {drink}")
            water = MENU[drink]["ingredients"]["water"]
            print(f"water: {water}")
            milk = MENU[drink]["ingredients"]["milk"]
            print(f"milk: {milk}")
            coffee = MENU[drink]["ingredients"]["coffee"]
            print(f"coffee: {coffee}")
            cost = MENU[drink]["cost"]
            print(f"cost: {cost}")

            return choice, water, milk, coffee, cost
        else:
            print("I'm just a simple coffee machine")
    return "This item is not on the menu"














# TODO 6 Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.


def check_payment(paid, drink):
    drink = ORDER
    change = 0.00
    cost = MENU[drink]["cost"]
    if paid < MENU[drink]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if paid > cost:
            #calculate change
            change = round((cost - paid), 2)
            print(f"Here is ${change} dollars in change.")
        else:
            print(f"Here is your {drink}.Enjoy!")
        # calculate report








# TODO 7 Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.



# TODO 2 Turn off the Coffee Machine by entering “off” to the prompt.
# For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

def turn_off(order):
    turned_on =  TURNED_ON
    order = ORDER
    if order == "off":
        turned_on = False
    else:
        turned_on = True
    return turned_on





















