class Pizza:

    def __init__(self, name, base, toppings):
        self.name = name
        self.base = base
        self.toppings = toppings

    def prices(self):
        self.base = 10
        self.toppings = self.toppings * 1.50
        total = self.base + self.toppings
        return total

    def display_info(self):
        print("---Welcome to the Pizza Parlor!---")
        print(f"hello, {self.name}!")
        print("Your total due amount is: $", self.prices())
        print("------------------------------")

toppings = 67
customer1 = Pizza("Han Maru", 1, toppings)
customer1.display_info()