MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report_show(money):
    print(f'''
                Water: {resources["water"]}ml \n
                Milk: {resources["milk"]}ml \n
                Coffee: {resources["coffee"]}g \n
                Money: ${money}
                ''')
        
def is_resources_sufficient(r):
    for key in r:
        if r[key] > resources[key]:
            print(f"Sorry not enough {key}")
            return False
    
    return True

def process_coins(q, d, n, p):
    quarters = 0.25
    dimes = 0.1
    nickles = 0.05
    pennies = 0.01

    return quarters * q + dimes * d + nickles * n + pennies * p

def make_coffee(coffee):
    for key in coffee:
        resources[key] -= coffee[key]

    return

money = 0
available_drink = list(MENU.keys())

# The prompt should be on repeat to serve the next customer
while True:
    print("Welcome to the Daily Coffee")
    print("What would you like today ? ☕ We have espresso/latte/cappuccino")
    #Check the user's input
  
    order = input("I'd like: ")
    

    #'off' is a secret keyword for maintainers
    if order == "off":
        break

    # report to know the current status of the machine
    elif order == "report":
        report_show(money)
    else:
        if order not in available_drink:
            print("Sorry we don't have it in the menu")
            continue
        drink = MENU[order]
        if is_resources_sufficient(drink["ingredients"]):
            quarters = float(input("Quarters: "))
            dimes = float(input("Dimes: "))
            nickles = float(input("Nickles: "))
            pennies = float(input("Pennies: "))
            payment = process_coins(quarters, dimes, nickles, pennies)
            if payment < drink["cost"]:
                print("Sorry that is not enough money 🫤. Money refunded")
                continue
            else:
                change =  payment - drink["cost"]
                money += payment
                make_coffee(drink["ingredients"])
                print(f"☕ Here's your {order} and ${round(change,2)} in change. Enjoy! ")
