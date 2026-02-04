# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

# 1) Subtract sales
for i in range(len(products)):
    products[i][1] -= units_sold[i][1]

# 2) Add shipments
for i in range(len(products)):
    products[i][1] += shipment_received[i][1]

# 3) Print result once
print("Final stock levels for all products:", products)


# Mistakes and Corrections
#for i in len(range(products)):
#     updated_stock = products - units_sold

# for y in len(range(products)):
#     shipment_received += updated_stock
#     print(f"Final stock levels for all products: {products}")

# 1. Incorrect use of range():
#    Mistake: for i in len(range(products)):
#    Fix:    for i in range(len(products)):
#
# 2. Wrong subtraction operation:
#    Mistake: updated_stock = products - units_sold
#    Fix:    products[i][1] -= units_sold[i][1]
#
# 3. Wrong addition operation and misplaced print:
#    Mistake: shipment_received += updated_stock
#             print(f"...{products}")
#    Fix:    products[i][1] += shipment_received[i][1]
#             print(...) should be after both loops, not inside the second loop
#
# 4. Loop variables and indexing:
#    - Use the same index variable (i) in both loops for consistency.
#    - Access the nested list elements via products[i][1], units_sold[i][1], shipment_received[i][1].
#
# Correct loop structure:
#   for i in range(len(products)):
#       products[i][1] -= units_sold[i][1]
#   for i in range(len(products)):
#       products[i][1] += shipment_received[i][1]
#   print("Final stock levels for all products:", products)
