""""
Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.
"""

money = 50
price = 15
tax = .03
left_money = money - (price+(price * tax))
print(left_money)