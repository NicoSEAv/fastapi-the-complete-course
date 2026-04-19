"""
Dictionaries
"""


user_dictionary = {
    'username': 'coding_with_roby',
    'name': 'Eric',
    'age': 32
}
print(user_dictionary.get('username'))
user_dictionary["married"] = True
print(user_dictionary)

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")
print(user_dictionary2)


"Per loopare su i dictionaries e' possbile usare il seguente metodo"
for x,y in user_dictionary.items():
    print(x,y)





















