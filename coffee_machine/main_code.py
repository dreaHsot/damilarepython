import coffee_recipe

def stock_refill(n):
    coffee_recipe.stock["espresso"] = n
    coffee_recipe.stock["steamed milk"] = n
    coffee_recipe.stock["foamed milk"] = n
    coffee_recipe.stock["chocolate"] = n

    print(f"done! stock refilled to {n}ml successfully")

def preparation(choice):
    



coffee = coffee_recipe.coffee_list
coffee_option = []
for i in coffee:
    coffee_option.append(i["name"])

print("select your coffee choice")
for i, c in enumerate(coffee_option):
    print(f"{i}: {c}")
p = input("Enter the index of your choice: ")
choice = coffee_option[p]