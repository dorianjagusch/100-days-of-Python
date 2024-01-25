from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


def main():
    while True:
        drink_type = input(f"What would you like to drink {menu.get_items()}?: ")
        if drink_type == "off":
            print("Bye bye...")
            break
        if drink_type == "report":
            coffee_maker.report()
            money_machine.report()
            continue
        drink = menu.find_drink(drink_type)
        if not coffee_maker.is_resource_sufficient(drink):
            continue
        if not money_machine.make_payment(drink.cost):
            continue
        coffee_maker.make_coffee(drink)


main()
