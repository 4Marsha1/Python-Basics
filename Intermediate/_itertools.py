# ITERTOOLS: product, permutations, combinations, accumulate, groupby, infinite iterators

# 1. product
# from itertools import  product
# a = [1,2]
# b = [3,4]
# prod = product(a,b)
# prod2 = product(a,b, repeat=2)
# print(list(prod))
# print(list(prod2))

# 2. permutations
# from itertools import permutations
# a = [1,2,3]
# perm = permutations(a)
# perm2 = permutations(a,2)
# print(list(perm))
# print(list(perm2))

# 3. combinations
# from itertools import combinations, combinations_with_replacement
# a = [1,2,3,4]
# comb = combinations(a,2)
# combR = combinations_with_replacement(a,2)
# print(list(comb))
# print(list(combR))

# 4. accumulate
# from itertools import accumulate
# import operator
# a = [1,2,3,4]
# acc = accumulate(a)         # DEFAULT
# print(list(acc))
# accMul = accumulate(a, func=operator.mul)
# print(list(accMul))
# b=[1,2,5,3,4,8,7]
# accMax = accumulate(b, func=max)
# print(list(accMax))

# 5. groupby
# from itertools import groupby
# a = [1,2,3,4]
# def smaller_than_3(x):
#     return x<3
# group_obj = groupby(a, key=smaller_than_3)
# for key, value in group_obj:
#     print(key, list(value))

# --------------EXAMPLE: 2
# persons = [{"name": 'John', "age": 21, "city": "Paris"}, {"name": 'Mary', "age": 17, "city": "Rome"},
#            {"name": 'Doe', "age": 13, "city": "Venice"}, {"name": 'Tim', "age": 21, "city": "Singapore"}]
#
# group_obj = groupby(persons, key=lambda x: x['age'])
# for key, value in group_obj:
#     print(key, list(value))

# 6. Infinite Iterators
# A. ------- Count
# from itertools import count
# for i in count(10):
#     print(i)
#     if i == 20:
#         break

# B. ------ Cycle
# from itertools import cycle
# a = [1,2,3,4,5]
# for i in cycle(a):
#     print(i)

# C. ------ Repeat
# from itertools import repeat
# for i in repeat(2):
#     print(i)
# for i in repeat(5,20):
#     print(i)