# SET: Unordered, mutable, no duplicates

# 1. Declaration
# mySet = {1,2,3,4}
# mySet2 = set([1,2,3,4])
# print(mySet, mySet2)
# mySet3 = set("Hello World!")
# print(mySet3)

# 2. Operations
# mySet = {1,2,3,4}
# mySet.add(5)
# print(mySet)
# mySet.pop()
# print(mySet)
# mySet.remove(3)
# print(mySet)
# mySet.discard(5)
# print(mySet)
# mySet.clear()
# print(mySet)

# 3. Looping
# mySet = {1,2,3,4,6}
# for x in mySet:
#     print(x)
# if 4 in mySet:
#     print("YES")

# 4. SET OPERATIONS
# set1 = {1,2,3,4,5,6,7,8,9}
# set2 = {1,2,3,10,11,12}

# UNION
# union = set1.union(set2)
# print(union)

# INTERSECTION
# intersection = set1.intersection(set2)
# print(intersection)

# DIFFERENCE
# diff = set1.difference(set2)
# print(diff)
# symmDiff = set1.symmetric_difference(set2)
# print(symmDiff)

# SUBSET & SUPERSET & DISJOINT
# setA = {1,2,3,4,5}
# setB = {1,2,3}
# print(setA.issubset(setB))
# print(setA.issuperset(setB))
# print(setA.isdisjoint(setB))

# 5. SET UPDATE ----> IN PLACE SET OPERATIONS
# set1.update(set2)                 # UNION
# print(set1)

# set1.intersection_update(set2)    # INTERSECTION
# print(set1)

# set1.difference_update(set2)      # DIFFERENCE
# print(set1)

# set1.symmetric_difference_update(set2) # SYMMETRIC DIFFERENCE
# print(set1)

# 6. COPYING
# mySet = {1,2,3,4}
# mySet_copy = mySet.copy()
# mySet_copy = set(mySet)


#### 7.  FROZEN SET------------------> IMMUTABLE SET
# myFrozenSet = frozenset([1,2,3,4])
# print(myFrozenSet)

