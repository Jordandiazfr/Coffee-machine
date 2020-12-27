MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "water": 300,  # 3000
    "milk": 200,
    "coffee": 100,
}
# Inicio del programa
dinero = float(0)
# check if the resources are available

def check_for_resources(drink):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    water_need = MENU[drink]['ingredients']['water']
    coffee_need = MENU[drink]['ingredients']['coffee']
    milk_need = MENU[drink]['ingredients']['milk']
    required_resources = [water_need, coffee_need, milk_need]
    if water_need > water:
        print("There is not enough water")
        return 0
    elif coffee_need > coffee:
        print("There is not enough coffee")
        return 0
    elif milk_need > milk:
        print("There is not enough milk")
        return 0
    else:
        return required_resources


def ask_money(type_of_coffee):
    print("Please insert coins")
    cost = MENU[type_of_coffee]["cost"]
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pannies?: "))
    coins = float((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
    if coins > cost:
        change = round(coins - cost, 2)
        print(f"You gave us ${coins} we give you back: ${change}")
        dinero = + cost
        return cost
    elif coins == cost:
        dinero = + cost
        return cost
    elif coins < cost:
        print("You didn't insert enough coins, money refunded")
        return 0


machine_on = True
# Machine start
while machine_on:
    # Test area
    # Get the user choice
    choice = input("What would you like to drink? ☕: (expresso [1] /latte [2] /capuccino[3]) ")
    if choice == "1":
        print("espresso on the making....")
        cafe = "espresso"
    elif choice == "2":
        print("latte on the making...")
        cafe = "latte"
    elif choice == "3":
        print("Cappuccino on the making...")
        cafe = "cappuccino"
    elif choice == "report":
        print("\nWater: %dml\nMilk: %dml\nCoffee: %dml" % (resources['water'], resources['milk'], resources['coffee']))
        print(f"Money: ${dinero}")
    elif choice == "off":
        machine_on = False
        print('Exit')
    else:
        print("Select a valid choice, 1,2 or 3 ")
    # Get the coin
    if choice == "1" or choice == "2" or choice == "3":
        is_there_enough = check_for_resources(cafe)
        if is_there_enough != 0:
            got_coin = ask_money(cafe)
            if got_coin != 0:
                # add the coin to dinero if the transaction is successful
                dinero += got_coin
                # substract the ressources
                new_water = resources['water'] - is_there_enough[0]
                new_coffee = resources['coffee'] - is_there_enough[1]
                new_milk = resources['milk'] - is_there_enough[2]
                resources.update(water=new_water, coffee=new_coffee, milk=new_milk)
                print("Here is your %s, ☕ Enjoy" % cafe)
