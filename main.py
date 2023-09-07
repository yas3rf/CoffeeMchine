from data import MENU, resources


def check_resources(coffee):
	for i in resources:
		if resources[i] > MENU[coffee]["ingredients"][i]:
			resources["water"] -= MENU[coffee]["ingredients"]["water"]
			resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
			resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
			return True
		else:
			return False


def make_coffee(coffee):

	print("Please insert coins.")
	quarters = int(input("how many quarters?  "))
	dimes = int(input("how many dimes?  "))
	nickels = int(input("how many nickles?  "))
	pennies = int(input("how many pennies?  "))
	total_coins = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

	if total_coins < MENU[coffee]["cost"]:
		print("money is not sufficient")

	elif total_coins > MENU[coffee]["cost"]:
		change = total_coins - MENU[coffee]["cost"]
		resources["coins"] = MENU[coffee]["cost"]
		print(f"your change is {round(change,2)}$ ")
		print(f"here is your {coffee} thanks")
	else:
		resources["coins"] = MENU[coffee]["cost"]
		print(f"here is your {coffee} thanks")
is_on = True
while is_on:
	user_choice = input("What would you like? (espresso: $1.5, latte: $2.5, cappuccino: $3) ")
	if user_choice == "off":
		is_on = False
	elif user_choice == "report":
		for resource in resources:
			print(f"{resource}: {resources[resource]}")

	elif user_choice == "espresso":
		if check_resources(user_choice):
			make_coffee(user_choice)
		else:
			print("Sorry not enough resources")
	elif user_choice == "latte":
		if check_resources(user_choice):
			make_coffee(user_choice)
		else:
			print("Sorry not enough resources")
	elif user_choice == "cappuccino":
		if check_resources(user_choice):
			make_coffee(user_choice)
		else:
			print("Sorry not enough resources")

	else:
		print("please insert valid order")
