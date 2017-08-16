"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
MENU= "To calculate your bonus please enter your sales"
print(MENU)
sales = float(input(">>> $"))
while sales < 0:
    print("Error please enter a possitive number")
    print(MENU)
    sales = float(input(">>> $"))
if  sales < 1000:
    bonus = sales * 0.1
else:
    bonus =  sales*0.15
print('Your bonus is: ${:.2f}'.format(bonus))



