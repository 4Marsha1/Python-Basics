import secrets

# Random INT below NUM (exclusive)
a = secrets.randbelow(10)
print(a)

# Random INT based on random Number of BITS
b = secrets.randbits(4)
print(b)

# On LISTS
myList = list('abcgdgfd')
choice = secrets.choice(myList)
print(choice)