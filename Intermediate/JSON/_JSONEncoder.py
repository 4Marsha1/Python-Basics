import json

person  = {"name": "John", "age": 28, "city":"Rome", "isAdult": True, "skills":["Coding", "Painting"]}
print(person)

# Encode into a variable
personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

# Encode into a file
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4, sort_keys=True)