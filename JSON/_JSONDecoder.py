import json

person = {"name": "John", "age": 28, "city":"Rome", "isAdult": True, "skills":["Coding", "Painting"]}
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# Decode into a variable
personDict = json.loads(personJSON)
print(personDict)

# Decode from a file
with open('person.json', 'r') as file:
    personDict2 = json.load(file)
    print(personDict2)