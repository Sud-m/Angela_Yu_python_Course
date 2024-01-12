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

COLLECTED_MONEY = 0


def printreport():
    """Print report of current resources and money collected in coffee machine."""
    water = RESOURCES["water"]
    milk = RESOURCES["milk"]
    coffee = RESOURCES["coffee"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${COLLECTED_MONEY}")


def check_ingredients(choice):
    """Check if coffee machine has enough ingredients."""
    current_ingredients = MENU[choice]["ingredients"]
    for ingredient in current_ingredients:
        if current_ingredients[ingredient] > RESOURCES[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def transaction_successful(choice):
    """Check if transaction is successful depending on coins inserted."""
    quarters = int(input("Please insert coins.\nHow many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    amount_entered = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    if amount_entered < MENU[choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    print(f"Here is ${amount_entered - MENU[choice]["cost"]} in change.")
    return True


def coffee_machine():
    """Actual coffee machine code"""
    while True:
        choice = input("What would you like? (espresso ($1.5)/ latte ($2.5)/ cappuccino ($3.0): ")
        if choice not in ["cappuccino", "latte", "espresso", "off", "report"]:
            print("Not a choice! Select again.\n")
        elif choice == "off":
            break
        elif choice == "report":
            printreport()
        else:
            if check_ingredients(choice):
                if transaction_successful(choice):
                    global COLLECTED_MONEY
                    print(f"Here is your {choice} ☕️. Enjoy!")
                    COLLECTED_MONEY += MENU[choice]["cost"]
                    for key in MENU[choice]["ingredients"]:
                        RESOURCES[key] -= MENU[choice]["ingredients"][key]


coffee_machine()
