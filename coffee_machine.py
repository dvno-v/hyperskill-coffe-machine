
class CoffeeMachine:

    def __init__(self, water, milk, coffee, cups, money):
        self.water = water
        self.milk  = milk
        self.coffee = coffee
        self.cups = cups
        self.money = money

    def has_enough_resources(self, needed_water, needed_coffee, needed_milk):

        res = 'I have enough resources, making you a coffee!'

        if self.water - needed_water < 0:

            res = 'Sorry, not enough water!'

        elif needed_milk != None and self.milk - needed_milk < 0:

            res = 'Sorry, not enough milk!'

        elif self.coffee - needed_coffee < 0:

            res = 'Sorry, not enough coffee!'

        elif self.cups <= 0:

            res = 'Sorry, not enough cups!'

        return res

    def print_machine_info(self):
        print(f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.coffee} of coffee beans\n{self.cups} of disposable cups\n${self.money} of money")

    def fill(self):

        print("Write how many ml of water do you want to add:")

        self.water += int(input())

        print("Write how many ml of milk do you want to add:")

        self.milk += int(input())

        print("Write how many grams of coffee beans do you want to add:")

        self.coffee += int(input())

        print("Write how many disposable cups of coffee do you want to add:")

        self.cups += int(input())


    def take(self):

        print(f"I give you ${self.money}")

        self.money = 0
    def order(self):

        res = ""

        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")

        order = input()

        #  For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.

        #  For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.

        #  And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.

        if order == '1':

            res = self.has_enough_resources(250, 16, None)

            if 'Sorry' in res:

                return res

            self.water -= 250

            self.coffee -= 16

            self.money += 4

        elif order == '2':

            res = self.has_enough_resources(350, 20, 75)

            if 'Sorry' in res:

                return res

            self.water -= 350

            self.milk -= 75

            self.coffee -= 20

            self.money += 7

        elif order == '3':

            res = self.has_enough_resources(200, 12, 100)

            if 'Sorry' in res:

                return res

            self.water -= 200

            self.milk -= 100

            self.coffee -= 12

            self.money += 6

        elif order == 'back':

            return 'back'



        self.cups -= 1

        return res
