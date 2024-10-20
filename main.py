MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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

def resource_report(resource):
    print("Displaying the report:")
    print(f"Water: {resource["water"]} ml")
    print(f"Milk: {resource["milk"]} ml")
    print(f"Coffee: {resource["coffee"]} gram")
    print(f"Money: ${profit}")

def check_enough_resource(resource , coffee_name, menu):
    water_req = menu[coffee_name]["ingredients"]["water"]
    milk_req = menu[coffee_name]["ingredients"]["milk"]
    coffee_req = menu[coffee_name]["ingredients"]["coffee"]

    if resource["water"]>=water_req and resource["milk"]>=milk_req and resource["coffee"]>=coffee_req:
        total_money = insert_coins()
        if check_money(MENU, coffee_name, total_money):
            resource["water"] -= water_req
            resource["milk"] -= milk_req
            resource["coffee"] -= coffee_req
    else:
        print("Sorry! Not enough resources")

def check_money(menu, coffee_name, m_inserted):
    coffee_cost = menu[coffee_name]["cost"]
    if m_inserted >= coffee_cost:
        global profit
        profit += coffee_cost
        print(f"Here's your change: ${round(m_inserted-coffee_cost,2)}")
        print(f"Enjoy your {coffee_name} ☕")
        return True
    else:
        print("Not enough money.")
        print(f"Money refunded ${m_inserted}")
        return False

def insert_coins():
    print("Insert the coins :-")
    penny = float(input("How many pennies ? "))
    nickel = float(input("How many nickel ? "))
    dime = float(input("How many dime ? "))
    quarter = float(input("How many quarter ? "))

    total_money_inserted = (penny*0.01) + (nickel*0.05) + (dime*0.10) + (quarter*0.25)
    return total_money_inserted


profit = 0
machine_on = True

while machine_on:
    # take order by showing the buttons
    choice = input("What would you like to have? (Espresso/Latte/Cappuccino/Report/OFF): ").lower()
    if choice == "off":
        machine_on = False
        print("Turning off the machine.")
    elif choice == "report":
        resource_report(resources)
    else:
        check_enough_resource(resources , choice, MENU)