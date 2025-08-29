import os
machine_info = [
    {
        "item": "latte",
        "water": 20,
        "milk": 45,
        "coffee": 60,
        "price": 120
    },
    {
        "item": "espresso",
        "water": 50,
        "milk": 20,
        "coffee": 0,
        "price": 200
    },
    {
        "item": "cappuccino",
        "water": 0,
        "milk": 37,
        "coffee": 80,
        "price": 230
    }
]


def check_latte(milk, coffee, water):
    if milk < 45:
        print("Not enough milk.")
        return False
    if coffee < 60:
        print("Not enough coffee.")
        return False
    if water < 20:
        print("Not enough water.")
        return False
    return True

def check_espresso(milk, water):
    if milk < 20:
        print("Not enough milk.")
        return False
    if water < 50:
        print("Not enough water.")
        return False
    return True

def check_cappuccino(milk, coffee):
    if milk < 37:
        print("Not enough milk.")
        return False
    if coffee < 80:
        print("Not enough coffee.")
        return False
    return True


def amount_collector():
    coins5 = int(input("How many 5rs coins: "))
    coins10 = int(input("How many 10rs coins: "))
    coins20 = int(input("How many 20rs coins: "))
    total = (coins5 * 5) + (coins10 * 10) + (coins20 * 20)
    return total


milk_left = 80
coffee_left = 100
water_left = 70
profit = 0

print(f"Latte = {machine_info[0]['price']} rs, Espresso = {machine_info[1]['price']} rs, Cappuccino = {machine_info[2]['price']} rs")

running_time = True
while running_time:
    user_input = input("What would you like? (latte/espresso/cappuccino/report/off): ").lower()

    if user_input == "latte":
        if check_latte(milk_left, coffee_left, water_left):
            money = amount_collector()
            if money >= machine_info[0]["price"]:
                milk_left -= 45
                coffee_left -= 60
                water_left -= 20
                profit += machine_info[0]["price"]
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Here is your Rs {money - machine_info[0]['price']} in change.")
                print("Here is your latte ☕")
            else:
                print("The amount is too low.")

    elif user_input == "espresso":
        if check_espresso(milk_left, water_left):
            money = amount_collector()
            if money >= machine_info[1]["price"]:
                milk_left -= 20
                water_left -= 50
                profit += machine_info[1]["price"]
                print(f"Here is your Rs {money - machine_info[1]['price']} in change.")
                print("Here is your espresso ☕")
            else:
                print("The amount is too low.")

    elif user_input == "cappuccino":
        if check_cappuccino(milk_left, coffee_left):
            money = amount_collector()
            if money >= machine_info[2]["price"]:
                milk_left -= 37
                coffee_left -= 80
                profit += machine_info[2]["price"]
                print(f"Here is your Rs {money - machine_info[2]['price']} in change.")
                print("Here is your cappuccino ☕")
            else:
                print("The amount is too low.")

    elif user_input == "report":
        print(f"Water: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}g\nProfit: {profit}rs")

    elif user_input == "off" or user_input == "q":
        print("Machine turned off.")
        running_time = False

    else:
        print("Enter a valid option.")
