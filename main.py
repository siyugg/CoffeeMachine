from data import *

def espresso():
    if resources['water']<MENU['espresso']['ingredients']['water']:
        print("Sorry, the water is insufficient.")
    elif resources['coffee']<MENU['espresso']['ingredients']['coffee']:
        print("Sorry, the coffee is insufficient.")
    else:
        print("Please insert coins: ")
        dollar = input("1 Dollar: ")
        fiftyC = input("50 Cents: ")
        twentyC = input("20 Cents: ")
        tenC = input("10 Cents: ")
        total = float(dollar) + (float(fiftyC) * 0.5) + (float(twentyC) * 0.2) + (float(tenC) * 0.1)
        cost = MENU['espresso']['cost']
        if total >= cost:
            change = total - cost
            print("Here's $" + str(change) + " in change")
            print("Here is your espresso ☕ Enjoy~")
            resources['water'] = resources['water'] - MENU['espresso']['ingredients']['water']
            resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
        elif total<cost:
            print("Sorry, not enough money. Money refunded")

def latte():

    if resources['water'] < MENU['latte']['ingredients']['water']:
        print("Sorry, the water is insufficient")
    elif resources['milk'] < MENU['latte']['ingredients']['milk']:
        print("Sorry, the milk is insufficient")
    elif resources['coffee'] < MENU['latte']['ingredients']['coffee']:
        print("Sorry, the coffee is insufficient")
    else:
        print("Please insert coins: ")
        dollar = input("1 Dollar: ")
        fiftyC = input("50 Cents: ")
        twentyC = input("20 Cents: ")
        tenC = input("10 Cents: ")
        total = float(dollar) + (float(fiftyC) * 0.5) + (float(twentyC) * 0.2) + (float(tenC) * 0.1)
        cost = MENU['latte']['cost']
        if total>=cost:
            change=total-cost
            print("Here's $" + str(change) + " in change")
            print("Here is your latte ☕ Enjoy~")
            resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
            resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']
        elif total<cost:
            print("Sorry, not enough money. Money refunded")

def cappuccino():
    if resources['water'] < MENU['cappuccino']['ingredients']['water']:
        print("Sorry, the water is insufficient")
    elif resources['milk'] < MENU['cappuccino']['ingredients']['milk']:
        print("Sorry, the milk is insufficient")
    elif resources['coffee'] < MENU['cappuccino']['ingredients']['coffee']:
        print("Sorry, the coffee is insufficient")
    else:
        print("Please insert coins: ")
        dollar = input("1 Dollar: ")
        fiftyC = input("50 Cents: ")
        twentyC = input("20 Cents: ")
        tenC = input("10 Cents: ")
        total=float(dollar)+(float(fiftyC)*0.5)+(float(twentyC)*0.2)+(float(tenC)*0.1)
        cost=MENU['cappuccino']['cost']
        if total>=cost:
            change=total-cost
            print("Here's $" + str(change) + " in change")
            print("Here is your cappuccino ☕ Enjoy~")
            resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
            resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['water']
            resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
        elif total<cost:
            print("Sorry, not enough money. Money refunded")

while(True):
    action=input("What would you like? (E: Espresso / L: Latte / C: Cappuccino): ")
    if action=='E':
        espresso()
    elif action=='L':
        latte()
    elif action=='C':
        cappuccino()
    elif action=='report':
        print(resources)



