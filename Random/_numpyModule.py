import numpy as np
# Used to generate random arrays


# Random Float Array with elements 0->1
a = np.random.random(3)
print(a)
b = np.random.random((3,5))         # (n,m)
print(b)

# Random INT Array with elements between Low & High
c = np.random.randint(10,100,(3,7))     # (Low, High, (n,m))
print(c)

# Shuffle array based on ROWS
np.random.shuffle(c)
print(c)

# ------- SEEDING --------
print("------- SEEDING --------")
np.random.seed(2)
print(np.random.random(3))
np.random.seed(1)
print(np.random.random(3))
np.random.seed(2)
print(np.random.random(3))
np.random.seed(1)
print(np.random.random(3))