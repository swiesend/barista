import unittest
from barista.coffee import *

class TestCoffee(unittest.TestCase):

    def test_coffee(self):
        names = [c.name for c in COFFEES]

        self.assertTrue('Americano' in names)
        self.assertTrue('Cappuccino' in names)
        self.assertTrue('Espresso' in names)
        self.assertTrue('Latte Macchiato' in names)
        self.assertTrue('Moccaccino' in names)

    def test_coffee_prices(self):
        for coffee in COFFEES:
            if coffee.name == 'Americano':
                self.assertEqual(coffee.price, 1.50)
            elif coffee.name == 'Cappuccino':
                self.assertEqual(coffee.price, 2.00)
            elif coffee.name == 'Espresso':
                self.assertEqual(coffee.price, 1.30)
            elif coffee.name == 'Latte Macchiato':
                self.assertEqual(coffee.price, 2.20)
            elif coffee.name == 'Moccaccino':
                self.assertEqual(coffee.price, 2.30)

    def test_machine_factors(self):
        for machine in MACHINES:
            if machine.name == 'Filter Machine':
                self.assertEqual(machine.factor, 1.0)
            elif machine.name == 'Pad Machine':
                self.assertEqual(machine.factor, 1.1)
            elif machine.name == 'Capsule Machine':
                self.assertEqual(machine.factor, 1.2)
            elif machine.name == 'Espresso Machine':
                self.assertEqual(machine.factor, 1.3)

    def test_calculate_total_price(self):
        self.assertEqual(calculate_total_price(1, 1.00, 1.00), 1.00)
        self.assertEqual(calculate_total_price(1, 1.00, 1.10), 1.10)
        self.assertEqual(calculate_total_price(1, 1.33, 1.00), 1.30)
        self.assertEqual(calculate_total_price(2, 1.33, 1.00), 2.70)
        self.assertEqual(calculate_total_price(3, 1.33, 1.00), 4.00)


if __name__ == '__main__':
    unittest.main()
