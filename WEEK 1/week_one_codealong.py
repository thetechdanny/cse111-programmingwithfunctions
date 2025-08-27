import datetime


quantity = -1
sub_total = 0

while quantity != 0:
    price = float(input("What is the price of the item: "))
    quantity = int(input("What is the quantity: "))
    
    per_sub_total = price * quantity
    sub_total += per_sub_total
    

today = (datetime.datetime.today().strftime('%A')).capitalize()


if sub_total >= 50 and (today == "Monday" or today == "Tuesday"):
    discount_value = sub_total * (10 / 100)
    tax_value = sub_total * (6 / 100)
    total_amount = (sub_total + tax_value) - discount_value
    print(f"Because you made a purchase of $50 or above and it is our discount day\nYour discount is {discount_value}, your tax is {tax_value} and you should pay {total_amount}")

elif sub_total != 50 and (today == "Monday" or today == "Tuesday"):
    needed_amount = 50 - sub_total
    tax_value = sub_total * (6 / 100)
    total_amount = (sub_total + tax_value)
    print(f"To receive a discount on our discount days, you must purchase at least $50 worth items")
    print(f"You need to purchase additional amount of {needed_amount} to receive our discount")
    print(f"Your tax is {tax_value} and your amount payable is {total_amount}")

else:
    tax_value = sub_total * (6 / 100)
    total_amount = (sub_total + tax_value)
    print(f"Your tax is {tax_value} and your amount payable is {total_amount}")
