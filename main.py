import coffee_machine

machine_water = 400

machine_milk = 540

machine_coffee = 120

machine_cups = 9

machine_money = 550

machine = coffee_machine.CoffeeMachine(machine_water, machine_milk, machine_coffee, machine_cups, machine_money)


print('Write action (buy, fill, take, remaining, exit):')

what_to_do = input()

while what_to_do != 'exit':

    if what_to_do == 'fill':

        machine.fill()

    elif what_to_do == 'take':

        machine.take()

    elif what_to_do == 'buy':

        res = machine.order()

        if res != 'back':

            print(res)

    elif what_to_do == 'remaining':

        machine.print_machine_info()

    print('Write action (buy, fill, take, remaining, exit):')

    what_to_do = input()
