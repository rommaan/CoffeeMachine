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

money = 0.00

turned_on = True

payment = 0.00

order = input("What would you like? (espresso/latte/cappuccino):")
if order == "espresso":
    resources["water"] -= 50
    resources["coffee"] -= 18
    money += 1.5
elif order == "latte":
    resources["water"] -= 200
    resources["milk"] -= 150
    resources["coffee"] -= 24
    money += 2.5
elif order == "cappuccino":
    resources["water"] -= 250
    resources["milk"] -= 100
    resources["coffee"] -= 24
    money += 3
elif order == "report":
    print(f" Water: {resources['water']}")
    print(f" Milk: {resources['milk']}")
    print(f" Coffee: {resources['coffee']}")
    print(f"Money: ${money}")
else:
    print("Could you please repeat what you'd like?")




# TODO 4 Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.


def check_resources():
# a. If there are sufficient resources to make the drink selected, then the program should


def accept_payment():
    print("Please insert coins!")
    quarters = int(input("How many quarters:  ")) * 0.25
    dimes = int(input("How many dimes:  ")) * 0.10
    nickles = int(input("How many nickles:  ")) * 0.05
    pennies = int(input("How many pennies:  ")) * 0.01
    payment = quarters + dimes + nickles + pennies
    print(f"You inserted ${payment}.")
    return payment


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


def check_payment():


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

if order == "off":
    turned_on = False
else:
    turned_on = True



















