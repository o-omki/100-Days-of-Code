from data import Menu

def resource_check(ordered_item):
    ingredients_required = ordered_item["ingredients"]
    for ingredient in ingredients_required:
        if ingredients_required[ingredient] > machine_resources[ingredient]:
            print(f"Sorry there isn't enough {ingredient} left in the machine for your order.")
            return False
    return True

def process_coins():
    print("Please insert the coins...")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction_check(money_inserted, drink_cost):
    if money_inserted < drink_cost:
        print("\nSorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_inserted - drink_cost, 2)
        print(f"\nHere's your ${change} change.")
        global profit
        profit += drink_cost
        return True

def make_coffee(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        machine_resources[ingredient] -= drink_ingredients[ingredient]
    print(f"\nHere's your {drink_name.title()} ☕️. Enjoy! \nThank You for using us!")



profit = 0
machine_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True

while is_on:
    order = input("\nWhat would you like? (espresso / latte / cappuccino): ").strip()
    if order == "off":
        is_on = False

    elif order == "report":
        print(f"Water: {machine_resources['water']}ml \
            \nMilk: {machine_resources['milk']}ml \
            \nCoffee: {machine_resources['coffee']}g \
            \nMoney: ${profit}")

    else:
        if order in Menu.keys():
            drink = Menu[order]
            if resource_check(drink):
                money_inserted = process_coins()
                if transaction_check(money_inserted, drink["cost"]):
                    make_coffee(order, drink["ingredients"])

        else:
            print("Sorry we don't have that drink.")

        