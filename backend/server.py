class Menu:

    def __init__(self):

        self.items = {
            "Espresso": 2.50,
            "Cappuccino": 4.50,
            "Freakshake": 5.00,
            "Black Tea": 1.50,
            "Green Tea": 2.00,
            "tea": 1.00,
            "plain sandwich": 3.00,
            "cheese sandwich": 3.50,
            "Grilled sandwich": 4.00,
            "aloo tikki burger": 5.00,
            "cheese burger": 5.50,
            "cheese and corn pizza": 6.00,
            "cheese burst pizza": 7.00,
            "chocolate cake": 4.00,
            "vanilla cake": 4.00
        }

    def display_items(self):
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f}")

    def get_price(self, item):
        return self.items.get(item)

    def total_cost(self, order_list):

        total = 0

        for item in order_list:
            if item in self.items:
                total += self.items[item]

        return total