from data import MENU, resources

MENU_ITEMS = ["off", "report", "espresso", "latte", "cappuccino"]
ACCEPTED_COINS = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "pennie": 0.01
}


def check_resources(drink_type):
    for key in MENU[drink_type]["ingredients"]:
        if resources[key] < MENU[drink_type]["ingredients"][key]:
            print(f"Not enough {key}.")
            return False
    return True


def insert_coins(drink_type, machine_money):
    total = 0
    print("Please insert coins.")

    for coin_type in ACCEPTED_COINS:
        amount = int(input(f"How many {coin_type}s?: "))
        total += ACCEPTED_COINS[coin_type] * amount
    cost = MENU[drink_type]["cost"]

    if total < cost:
        print(f"Not enough money. Returning: ${round(total - cost, 2)}")
        return False
    else:
        print(f"Here is your change: ${round(total - cost, 2)}")
        machine_money += cost
        return True


def make_drink(drink_type):
    for resource in MENU[drink_type]["ingredients"]:
        resources[resource] -= MENU[drink_type]["ingredients"][resource]
    print(f"Here is your {drink_type}. Enjoy!")
    return


def print_resources(coins):
    for key in resources:
        print(f"{key.title()}: {resources[key]}")
    print(f"Money: ${round(coins, 2)}")
    return


def coffee_machine():
    coins = 0
    while True:
        drink_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if drink_type == "off":
            print("Turning off...")
            return
        if drink_type == "report":
            print_resources(coins)
            continue
        if drink_type not in MENU_ITEMS:
            print("Please select from 'espresso', 'latte', 'cappuccino'")
            continue

        if not check_resources(drink_type):
            continue
        if not insert_coins(drink_type, coins):
            continue
        coins += MENU[drink_type]["cost"]
        make_drink(drink_type)


coffee_machine()
