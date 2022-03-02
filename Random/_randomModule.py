import random

# Random Float between 0 & 1
a = random.random()
print(a)

# Random Float between Low & High
b = random.uniform(0,100)
print(b)

# Random Int between Low & High [Low, High]
c = random.randint(0,20)
print(c)

# Random Int between Low & High [Low, High)
d = random.randrange(0, 100, 15)
print(d)

# Mean & standard deviation
e = random.normalvariate(0, 1)
print(e)

# -------------- On LISTS

# Single Choice
myList = list('abcdefgij')
f = random.choice(myList)
print(f)

# List of Choices
# Without repetition
g = random.sample(myList, 4)
print(g)

# With repetition
h = random.choices(myList, k=4)
print(h)

# Shuffle list
print(myList)
random.shuffle(myList)
print(myList)


# -------------------- SEEDING
print("------------SEEDING---------")
random.seed(1)
print(random.random())
random.seed(2)
print(random.random())
random.seed(1)
print(random.random())
random.seed(2)
print(random.random())