"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly brackets
"""

my_set = {1, 2, 3, 4, 5, 1, 2}
print("my_set")
print(my_set)
print("len(my_set)")
print(len(my_set))
#
#
print("looping over my_set")
for item in my_set:
    print(item)
#

print("discarding an element from my_set")
my_set.discard(3)
print(my_set)
# my_set.add(6)
# print(my_set)
# my_set.update([7, 8])
# print(my_set)

print("------- TUPLES -------")
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
# my_tuple[1] = 100
























