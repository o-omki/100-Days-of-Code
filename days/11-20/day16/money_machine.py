class MoneyMachine:
    CURRENCY = '$'
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes" : 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")
    
    def _process_coins(self):
        print("Please insert the coins...")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received 
    
    def make_payment(self, drink_cost):
        self._process_coins()
        if self.money_received >= drink_cost:
            change = round(self.money_received - drink_cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += drink_cost
            self.money_received = 0
            return True
        else:
            print(f"Sorry that's not enough money. Money refunded.")
            return False
