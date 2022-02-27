import sys
import timeit

# Check Space Occupied
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# Check Time taken for Creation
print(timeit.timeit(stmt="[1,2,3,4,5]", number=10000000))
print(timeit.timeit(stmt="(1,2,3,4,5)", number=10000000))