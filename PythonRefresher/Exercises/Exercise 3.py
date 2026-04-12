"""
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
"""

zoo = ["hippo", "lion", "tiger", "elephant", "zebra"]
print(zoo)

zoo.pop(3)
print("\nDelete the animal at the 3rd index.")
print(zoo)

zoo.append("giraffa")
print("\nAppend a new animal at the end of the list")
print(zoo)

zoo.pop(0)
print("\nDelete the animal at the beginning of the list")
print(zoo)

print("\nPrint all the animals:")
for animal in zoo:
    print(animal)

print("\nPrint only the first 3 animals")
print(zoo[0:3])