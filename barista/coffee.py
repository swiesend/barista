
class Coffee(object):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

COFFEES = [Coffee('Americano', 1.50),
           Coffee('Cappuccino', 2.00),
           Coffee('Espresso', 1.30),
           # Coffee('Latte Macchiato', 2.20),
           Coffee('Moccaccino', 2.30),]


class CoffeeMachine(object):
    def __init__(self, name: str, factor: float = 1.0):
        self.name = name
        self.factor = factor

MACHINES = [CoffeeMachine('Filter Machine'),
            CoffeeMachine('Pad Machine', 1.1),
            CoffeeMachine('Capsule Machine', 1.2),
            CoffeeMachine('Espresso Machine', 1.3),]


def calculate_total_price(amount: int, price: float, factor: float):
    return round(amount * price * factor, 1)


def make_coffee(amount: int, coffee: Coffee, machine: CoffeeMachine):
    if amount < 1:
        return 'Your ordered {} coffees. How many coffees again, please?'.format(amount)
    else:
        total = calculate_total_price(amount, coffee.price, machine.factor)
        if amount == 1:
            return 'Made one {} with a {} for only {:.2f}€.'.format(coffee.name, machine.name, total)
        else:
            return 'Made {} {}s with a {} for only {:.2f}€.'.format(amount, coffee.name, machine.name, total)
