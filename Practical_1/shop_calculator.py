<<<<<<< HEAD


no_of_items = int(input("How many items: "))

while no_of_items <= 0:
    print("Invalid Number of Items")
    no_of_items = int(input("How many items: "))

total_price = 0
for i in range(0, no_of_items, 1):
    single_price = float(input("Price of item: "))
    total_price = total_price + single_price

if total_price > 100:
    total_price = total_price * 0.9

print("Total price for", no_of_items, "items is", f"${total_price:,.2f}")
=======


no_of_items = int(input("How many items: "))

while no_of_items <= 0:
    print("Invalid Number of Items")
    no_of_items = int(input("How many items: "))

total_price = 0
for i in range(0, no_of_items, 1):
    single_price = float(input("Price of item: "))
    total_price = total_price + single_price

if total_price > 100:
    total_price = total_price * 0.9

print("Total price for", no_of_items, "items is", f"${total_price:,.2f}")
>>>>>>> efb4c5ef487ad18a03dd9b8d1be76683032a0863
