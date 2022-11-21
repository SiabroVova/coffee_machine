MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 20,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 35,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 45,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_enough(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please input coins.")
    total = int(input("How many UAH?: "))
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when payment is enough for chosen drink and False if not."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ₴{change} is your rest.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded. ")
        return False


def make_coffee(drink_name, order_ingredients):
    """Func for coffee preparation. It will minus ingredients from resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is you {drink_name} ☕")


is_on = True
while is_on:
    choice = input("What would you ike? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ₴{profit}")
    else:
        drink = MENU[choice]
        if is_resource_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
