#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""
Item1 = input("Enter in price of item #1:")
Item2 = input("Enter in price of item #2:")
Item3 = input("Enter in price of item #3:")
Item4 = input("Enter in price of item #4:")
Item5 = input("Enter in price of item #5:")
Item1 = float(Item1)
Item2 = float(Item2)
Item3 = float(Item3)
Item4 = float(Item4)
Item5 = float(Item5)


total=0.0

subtotal=Item1 + Item2 + Item3 + Item4 + Item5
print(f"Your subtotal {subtotal}")
GST= subtotal*0.05
GST = round(GST,2)
print(f"Your GST is {GST}")
PST = subtotal*0.07
PST = round(PST,2)
print(f"Your PST is {PST}")
total = total + subtotal + GST +PST
total = round(total,2)
print(f"Your total is {total}")