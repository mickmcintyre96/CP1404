
number_of_items = int(input('How Many Items?'))
total = 0
while number_of_items < 0:
    print("Invalid number of items, please try again")
    number_of_items = int(input('How Many Items? '))
for i in range(1, number_of_items + 1):
    print("What is the price of item no.", i, )
    price = float(input("$"))
    total = total + price
if total > 100:
    total = total * 0.9
# print the total price and number of items
if number_of_items > 1:
    print("Total price of", number_of_items, "items is ${:.2f}".format(total))
else:
    print("Total price of 1 item is ${:.2f}".format(total))
