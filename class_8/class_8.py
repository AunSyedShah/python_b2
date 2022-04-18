total = 0

while True:
    item_price = float(input("Enter the price of the item: "))
    if item_price < 1:
        break
    total = total + item_price

print(f"The total is {total}")