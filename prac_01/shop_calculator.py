"""Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92  """
total = 0
items = int(input("Number of items: "))
while items <= 0:
    print("You must have at least one item.")
    items = int(input("Number of items: "))
for i in range(items):
    price = float(input("Price of item: "))
    total = total + price
if total > 100:
    print("You are eligible for a 10% discount for your total price of items.")
    total = total * 0.9
else:
    print("You are not eligible for a discount for your total price of items.")
    total = price
print("Total price for {} items is ${:.2f}".format(items, total))
