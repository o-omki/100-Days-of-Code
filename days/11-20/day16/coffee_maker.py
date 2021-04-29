class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
    def report(self):
        print(f"Water: {self.resources['water']}ml \
                \nMilk: {self.resources['milk']}ml \
                \nCoffee: {self.resources['coffee']}g")
    
    def check_resources(self, drink):
        flag = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there isn't enough {item} left for your order.")
                flag = False
            return flag

    def make_coffee(self, drink_ordered):
        for item in drink_ordered.ingredients:
            self.resources[item] -= drink_ordered.ingredients[item]
        print(f"Here's your {drink_ordered.name} ☕️. Enjoy!")