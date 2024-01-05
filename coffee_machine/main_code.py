import coffee_recipe

def report():
    for i, q in coffee_stock.items():
        print(f"{i} : {q}")

    print(f"\nSales = {coffee_recipe.sales}")

def stock_refill(n):
    coffee_stock["espresso"] = n
    coffee_stock["steamed milk"] = n
    coffee_stock["foamed milk"] = n
    coffee_stock["chocolate"] = n

    print(f"done! stock refilled to {n}ml successfully")

def preparation(choice):
    for i in coffee:
        if i["name"] == choice:
            prepared_coffee = i
            coffee_stock["espresso"] -= i["espresso"]
            coffee_stock["steamed milk"] -= i["steamed milk"]
            coffee_stock["foamed milk"] -= i["foamed milk"]
            coffee_stock["chocolate"] -= i["chocolate"]

            payment = i["price"]
            coffee_recipe.sales += i["price"]

    print(f"{choice} coffee prepared for ${payment}\n")
    qq = input("do you want anything extra?(y/n): ").lower()

    if qq == 'n':
        print("Thank you; you can have your coffee now\n\n\n")
        return prepared_coffee
    elif qq == 'y':
        recipe = []
        for i, c in enumerate(coffee_stock.keys()):
            print(f"{i}: {c}")
            recipe.append(c)
        x = int(input("Enter the index of what you want to add;(0, 1, 2 or 3): "))
        extra = recipe[x]
        coffee_stock[extra] -= 5
        prepared_coffee[extra] += 5
        coffee_recipe.sales += (coffee_recipe.price_dict[extra] * 5)
        payment += (coffee_recipe.price_dict[extra] * 5)

        print(f"{choice} coffee prepared with selected extras for a total of {payment}")

        return prepared_coffee

power_on = True
coffee = coffee_recipe.coffee_list
coffee_stock = coffee_recipe.stock
coffee_option = []
for i in coffee:
    coffee_option.append(i["name"])

while power_on:
    print("select your coffee choice")
    for i, c in enumerate(coffee_option):
        print(f"{i}: {c}")

        
    p = input("Enter the index of your choice: ").upper()

    if p in ['0', '1', '2', '3', '4', '5', '6', '7']:
        choice = coffee_option[int(p)]
        preparation(choice)
    elif p == "REFILL":
        n = int(input("level refilled to: "))
        stock_refill(n)
    elif p == "REPORT":
        report()
    elif p == "OFF":
        power_on = False
    else:
        print("INVALID INPUT; TRY AGAIN")