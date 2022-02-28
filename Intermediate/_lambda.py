# LAMBDA FUNCTIONS :
# lambda arguments : expression

# 1. Simple lambda function
# add_two_nums = lambda x,y: x+y
# print(add_two_nums(10,20))

# 2. Sorted Function ---------------> sorted(sequence, key=func)
# points2D = [(1,2), (15,1), (-2,3), (-9,0)]
# print(points2D)

# points2D_sorted = sorted(points2D)      # by default: SORTED by X
# print(points2D_sorted)

# sort_by_y = sorted(points2D, key=lambda x: x[1])    # SORT by Y
# print(sort_by_y)

# sort_by_sum = sorted(points2D, key=lambda x: x[0]+x[1]) # SORT by SUM of X,Y
# print(sort_by_sum)

a = [1,2,3,4,5]
# 3. MAP function --------------> map(func, sequence)
# b = map(lambda x:x*2, a)     # Multiply by 2
# print(list(b))

# SIMILAR as --------  LIST COMPREHENSION METHOD
# b = [x*2 for x in a]
# print(b)

# 4. FILTER function ------------> filter(func, sequence)
# b = filter(lambda x:xS

# SIMILAR as ------- LIST COMPREHENSION METHOD
# b = [x for x in a if x%2==0]
# print(b)

# 5. REDUCE function ------------> reduce(func, sequence)
# from functools import reduce
# prod_a = reduce(lambda x,y: x*y, a)
# print(prod_a)