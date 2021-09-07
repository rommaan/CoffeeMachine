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






money = 0.00


# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
def prompt():
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    return drink


# TODO 2. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
#get each ingredient name and quantity out of the drink ordered

#check if the ingredient's name is in the resources names

#compare each ingredient's quantity with resource quantity
#if ingredient's quantity < resource quantity: continue to coins todo3.
#if ingredient's quantity > resource quantity: stop the process.
# print: “Sorry there is not enough water.”


# TODO 3. Process coins.

def accept_coins():
    print("Please insert coins!")
    quarters = int(input("How many quarters:  ")) * 0.25
    dimes = int(input("How many dimes:  ")) * 0.10
    nickles = int(input("How many nickles:  ")) * 0.05
    pennies = int(input("How many pennies:  ")) * 0.01
    payment = quarters + dimes + nickles + pennies
    print(f"You inserted ${payment}.")
    return payment



# TODO 4. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered.
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
#E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
def check_payment(drink, payment, balance = money):
    change = 0.0
    if drink == "espresso":
        if payment < MENU["espresso"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            balance += MENU["espresso"]["cost"]
            change = round((payment - MENU["espresso"]["cost"]), 2)
            print(f"Here is your {drink}.Enjoy!")
            print(f"Here is ${change} dollars in change.")
            return change
    elif drink == "latte":
        if payment < MENU["latte"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = round((payment - MENU["latte"]["cost"]), 2)
            print(f"Here is your {drink}.Enjoy!")
            print(f"Here is ${change} dollars in change.")
            return change
    elif drink == "cappuccino":
        if payment < MENU["cappuccino"]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = round((payment - MENU["cappuccino"]["cost"]), 2)
            print(f"Here is your {drink}.Enjoy!")
            print(f"Here is ${change} dollars in change.")
            return change
    else:
        print(f"no such drink as {drink} exists")





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

def recalculate_resources(drink):
    drink = ORDER
    resources = RESOURCES
    if drink == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        print(f"Water: {resources['water']}")
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        print(f"Coffee: {resources['coffee']}")
    elif drink == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        print(f"Water: {resources['water']}")
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        print(f"Milk: {resources['milk']}")
        resources["coffee"] -= MENU["latte"]["ingredients"]["milk"]
        print(f"Coffee: {resources['coffee']}")
    elif drink == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        print(f"Water: {resources['water']}")
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        print(f"Milk: {resources['milk']}")
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["milk"]
        print(f"Coffee: {resources['coffee']}")
    else:
        print("No such drink")
    return resources



def recalculate_balance(drink):
    drink = ORDER
    balance = BALANCE
    balance_addition = 0.00
    for choice, value in MENU.items():
        if drink == value:
            balance_addition = MENU[choice]["cost"]
            balance += balance_addition
            print(f"Balance : {balance}")
            return balance
    return "no such drink in the machine"


def report():
    balance = BALANCE
    resources = RESOURCES

    print(f"Your new balance is ${balance}")
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")







# TODO 4 Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.


def check_resources():
    drink = ORDER
    select_drink(drink)
    recalculate_resources(drink)
    if choice




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





















