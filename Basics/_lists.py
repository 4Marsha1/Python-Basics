# lists can have items of any data-type
list = [90, "Mark", 'A', 14.67, True]
print(list)

ages = [18, 21, 45, 92]
print(ages)
# indexing
print(ages[3])
print(ages[-4])
print(ages[1])
print(ages[-2])

# Slicing
newAges = ages[0:3]
print(newAges)

# For loop in list
for age in ages:
    print("==", age)