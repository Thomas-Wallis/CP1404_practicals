num_of_items = int(input("Number of items: "))
total_price = 0
item_list = []
while num_of_items < 0:
    print("Invalid number of items!")
    num_of_items = int(input("Please enter a valid number of items (0+): $"))
for item in range(0, num_of_items, 1):
    item_price = float(input("Please enter the price of item {}: ".format(item + 1)))
    item_list.append(item_price)
for item in item_list:
    print("Price of item: ${:,.2f}".format(item))
    total_price += item
print("Total price for {} items is ${:,.2f}".format(len(item_list), total_price))