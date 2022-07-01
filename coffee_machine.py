from resources import *

profit = 0.0
inserted_amount = 0
machine_on = True


def user_deposit():
    total = 0
    total += float(input("how many quarters?: ")) * 0.25
    total += float(input("how many dimes?: ")) * 0.10
    total += float(input("how many nickles?: ")) * 0.05
    total += float(input("how many pennies?: ")) * 0.01
    return total


def check_transaction(deposited_coins):
    if deposited_coins >= MENU[user_choice]["cost"]:
        return True
    else:
        return False


def handle_change(deposited_coins):
    change_return = deposited_coins - MENU[user_choice]["cost"]
    format_float = "{:.2f}".format(change_return)
    return format_float


def handle_resources():
    selection_ingredients = MENU[user_choice]["ingredients"]
    if (resources["water"] > selection_ingredients["water"]) and (resources["coffee"] > selection_ingredients["coffee"]):
        if user_choice == "espresso":
            resources["water"] -= selection_ingredients["water"]
            resources["coffee"] -= selection_ingredients["coffee"]
        else:
            if resources["milk"] > selection_ingredients["milk"]:
                resources["water"] -= selection_ingredients["water"]
                resources["coffee"] -= selection_ingredients["coffee"]
                resources["milk"] -= selection_ingredients["milk"]
            else:
                problem = ""
                if not resources["water"] > selection_ingredients["water"]:
                    problem += "water"
                elif not resources["coffee"] > selection_ingredients["coffee"]:
                    problem += "coffee"
                elif not resources["milk"] > selection_ingredients["milk"]:
                    problem += "milk"
                return problem
    else:
        problem = ""
        if not resources["water"] > selection_ingredients["water"]:
            problem += "water"
        elif not resources["coffee"] > selection_ingredients["coffee"]:
            problem += "coffee"
        elif not resources["milk"] > selection_ingredients["milk"]:
            problem += "milk"
        return problem


while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        machine_on = False
        break
    elif user_choice == "report":
        print("Water: " + str(resources["water"]) + "ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print("Money: " + str(profit) + "$")
        continue

    print("Please insert coins.")
    inserted_amount += user_deposit()

    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        if check_transaction(inserted_amount):
            if handle_resources() == "water" or handle_resources() == "milk" or handle_resources() == "coffee":
                print("Sorry, there is not enough " + handle_resources())
                machine_on = False
                break
            else:
                change = handle_change(inserted_amount)
                profit += MENU[user_choice]["cost"]
                print("Here is your " + user_choice + ". Enjoy ! ☕️")
                print("Here is $" + str(change) + " in change.")
        else:
            print("Sorry that's not enough money. Money refunded.")
