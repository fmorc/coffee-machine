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
    "money": 0
}


def turn_off():
    """Turns off the coffee machine"""
    exit()


def print_report():
    """Prints the current status of the coffee machine"""
    print(f"{resources['water']}ml")
    print(f"{resources['milk']}ml")
    print(f"{resources['coffee']}g")
    print(f"${resources['money']}")


def can_make_coffee(coffee) -> bool:
    """Check if the coffee machine has enough resources for the coffee selection and returns a boolean to indicate"""
    can_make = True
    ingredients = coffee["ingredients"]
    if ingredients["water"] > resources["water"]:
        can_make = False
        print("Sorry there is not enough water")
    if "milk" in ingredients and ingredients["milk"] > resources["milk"]:
        can_make = False
        print("Sorry there is not enough milk")
    if ingredients["coffee"] > resources["coffee"]:
        can_make = False
        print("Sorry there is not enough coffee")
    return can_make


def process_coins() -> float:
    """Returns the total values of the coin inputs"""
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return round(quarters*.25 + dimes*.10 + nickels*.05 + pennies * 0.1, 2)


def is_transaction_successful(coffee_selection):
    total = process_coins()
    coffee = MENU[coffee_selection]
    transaction_successful = False
    if coffee["cost"] > total:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if can_make_coffee(coffee):
            change = total - coffee["cost"]
            print(f"Here is ${change} in change.")
            print(f"Here is your {coffee_selection} ☕️. Enjoy")
            transaction_successful = True
    return transaction_successful


def update_resources(ingredients):
    resources["water"] = resources["water"] - ingredients["water"]
    if "milk" in ingredients:
        resources["milk"] = resources["milk"] - ingredients["milk"]
    resources["coffee"] = resources["coffee"] - ingredients["coffee"]


def update_earnings(cost):
    resources["money"] += cost


def coffee_machine():
    while True:
        coffee_selection = input("What would you like? (espresso/latte/cappuccino): ")
        if coffee_selection == 'report':
            print_report()
        elif coffee_selection == 'off':
            turn_off()
        else:
            if is_transaction_successful(coffee_selection):
                update_resources(MENU[coffee_selection]["ingredients"])
                update_earnings(MENU[coffee_selection]["cost"])


coffee_machine()