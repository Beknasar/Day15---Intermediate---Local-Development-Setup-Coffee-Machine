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


def make_coffee(resources, coffee):
    for key in coffee['ingredients'].keys():
        resources[key] -= coffee['ingredients'][key]
    print(f"Here is your {choice} ☕. Enjoy!")
    return resources


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money}")


def check_resourse(coffee):
    for ingredient, amount in resources.items():
        if ingredient not in coffee['ingredients']:
            continue
        elif coffee['ingredients'][ingredient] > amount:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def process_coins():
    print("Please insert coins")
    for key, value in coins.items():
        coins[key] = int(input(f"how many {key}?: "))
    quarters, dimes, nickles, pennies = coins.values()
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


def transaction(coffee, total):
    if coffee['cost'] <= total:
        total -= coffee['cost']
        print(f"Here is your ${round(total, 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


is_on = True
money = 0

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        is_on = False
    # TODO 3.  Print report.
    elif choice == "report":
        report()
    else:
        # TODO 4. Check resources sufficient?
        coffee = MENU[choice]
        is_correct = check_resourse(coffee)

        if is_correct:
            coins = {
                "quarters": 0,
                "dimes": 0,
                "nickles": 0,
                "pennies": 0
            }

            # TODO 5. Process coins.
            total_amount = process_coins()

            # TODO 6. Check transaction successful?
            is_successfull = transaction(coffee, total_amount)
            if is_successfull:
                money += coffee['cost']
                # TODO 7. Make Coffee.
                resources = make_coffee(resources, coffee)
            total_amount = 0


