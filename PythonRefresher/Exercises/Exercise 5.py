"""
Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

- Create a while loop that prints all elements of the my_list variable 3 times.

- When printing the elements, use a for loop to print the elements

- However, if the element of the for loop is equal to Monday, continue without printing
"""

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i=1
while i<4:
    print(f"Valori stampati {i}")

    for day in my_list:
        if day == "Monday":
            continue
        print(day)

    i += 1