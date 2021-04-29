class MenuItem:
    def __init__(self, name, cost, water, milk, coffee):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("latte", 2.5, 200, 150, 24),
            MenuItem("espresso", 1.5, 50, 0, 18),
            MenuItem("cappuccino", 3, 250, 50, 24)
        ]
    
    def get_drinks(self): 
        drink_names = ""
        for drink in self.menu:
            drink_names += f"{drink.name}/"
        return drink_names

    def find_drink(self, drink_ordered):
        for drink in self.menu:
            if drink.name == drink_ordered:
                return drink
            
        print(f"Sorry {drink_ordered.title()} is not available.")