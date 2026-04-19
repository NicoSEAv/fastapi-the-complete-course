"""
Create a function that takes in 3 parameters(firstname, lastname, age) and returns
a dictionary based on those values
"""


def create_dictionary(firstname,lastname, age):
    new_dictionary ={
        "firstname": firstname,
        "lastname": lastname,
        "age":age
    }
    return new_dictionary

print(create_dictionary('Nico', 'Buonfrate','28'))