"""
For & While Loops
"""

my_list = [1,2,3,4,5]

print("---- FOR LOOP ----")
for element in my_list:
    print(element)

print("---- FOR LOOP in RANGE ----")
for element in range(3,7):
    print(element)

print("---- FOR LOOP SUM OF THE ELEMENTS----")
sum_of_loop =0
for element in my_list:
    sum_of_loop +=element
print(sum_of_loop)


print("---- FOR LOOP STRINGS ----")

string_list = ["Monday","Tuesday","Wednesday"]

for string in string_list:
    print(f"Happy {string}!")


print("---- WHILE LOOP ----")
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
       break
else:
    print("i is now larger or equal to 5")



















