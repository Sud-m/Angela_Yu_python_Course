from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import os

main_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()


def kaapi():
    os.system("cls")
    while True:
        choice = input("What would you like? (espresso ($1.5)/ latte ($2.5)/ cappuccino ($3.0): ")

        if choice not in ["cappuccino", "latte", "espresso", "off", "report"]:
            print("Not a choice! Select again.")

        elif choice == "off":
            os.system("cls")
            print("Goodbye!")
            break

        elif choice == "report":
            coffee_machine.report()

        else:
            menu_choice = main_menu.find_drink(choice)
            if coffee_machine.is_resource_sufficient(menu_choice):
                if money_machine.make_payment(menu_choice.cost):
                    coffee_machine.make_coffee(menu_choice)


kaapi()
