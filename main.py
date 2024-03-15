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
    ingredient = list(resources.keys())
    print(f'''
                {ingredient[0]}: {resources[0]}ml \n
                {ingredient[1]}: {resources[1]}ml \n
                {ingredient[2]}: {resources[2]}g \n
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


money = 0

# The prompt should be on repeat to serve the next customer
while True:
    print("Welcome to the Daily Coffee")
    print("What would you like today ? ☕ We have espresso/latte/cappuchino")
    #Check the user's input
    order = input("I'd like: ")

    #'off' is a secret keyword for maintainers
    if order == "off":
        break

    # report to know the current status of the machine
    elif order == "report":
        report_show(money)
    else:
        drink = MENU[order]
        if is_resources_sufficient(drink["ingredients"]):
            quarters = float(input("Quarters: "))
            dimes = float(input("Dimes: "))
            nickles = float(input("Nickles: "))
            pennies = float(input("Pennies: "))
            process_coins(quarters, dimes, nickles, pennies)
    