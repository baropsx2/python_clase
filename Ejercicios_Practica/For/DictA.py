person = {
    'name': 'Oscar',
    'age': 36,
    'telephone': 3331235468
}
stuff = person.keys()

person['identification'] = 1234

for keys in stuff:
    print(keys)

valores = person.values()

for characteristics in valores:
    print(characteristics)
