from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
americano = MenuItem("americano", 100, 0, 50, 1.5)
CoffeeMaker = CoffeeMaker()
MoneyMachine = MoneyMachine()
is_on = True

# The prompt should be on repeat to serve the next customer
while is_on:
    print("Welcome to the Daily Coffee")

    available = menu.get_items()
    #Check the user's input
  
    order = input(f"What would you like today ? We have {available}: ")
    

    #'off' is a secret keyword for maintainers
    if order == "off":
        is_on = False
        continue

    # report to know the current status of the machine
    elif order == "report":
        CoffeeMaker.report()
        MoneyMachine.report()
    else:
        drink = menu.find_drink(order)
        if drink == None:
            continue

        if CoffeeMaker.is_resource_sufficient(drink):
            payment = MoneyMachine.make_payment(drink.cost)
            if payment:
                CoffeeMaker.make_coffee(drink)
            