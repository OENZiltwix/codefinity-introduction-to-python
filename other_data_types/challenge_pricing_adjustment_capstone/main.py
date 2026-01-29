grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8 ),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
}

eggs_info = grocery_inventory.get("Eggs")
eggs_price = eggs_info[1]
print(eggs_price)

if eggs_price > 5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = (
        eggs_info[0],
        eggs_price - 1,
        eggs_info[2]
    )
else:
    print("The price of Eggs is reasonable.")    

grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

milk_cat, milk_price, milk_stock = grocery_inventory["Milk"]
if milk_stock < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (milk_cat, milk_price, milk_stock + 20)
else:
    print("Milk has sufficient stock.")


print(f"Updated inventory: {grocery_inventory}")