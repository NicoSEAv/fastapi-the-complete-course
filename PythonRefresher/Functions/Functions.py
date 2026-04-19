"""
Functions
"""

def my_function():
    print("Inside my function")

my_function()

def print_my_name(name):
    print(f"Hello {name}!")

print_my_name("Nico")


def print_list(list_numbers):
    for x in list_numbers:
        print(x)

print_list([1,2,3,4,5])

def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate


final_cost = buy_item(50)
print(final_cost)














