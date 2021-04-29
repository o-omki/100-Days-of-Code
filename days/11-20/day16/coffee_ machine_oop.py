from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_switch = True

while machine_switch:
    drinks_list = menu.get_drinks()
    choice = input(f"What would you like to order? ({drinks_list[:-2]})")
    if choice == "off":
        machine_switch = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.check_resources(drink) and  money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
