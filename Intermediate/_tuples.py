# TUPLES: Ordered, immutable, allows duplicate elements

# 1. Declaration
# my_tuple = ("John", 21, "Vatican")
# my_tuple2 = "Max", 24, "Paris"
# my_tuple3 = ("One Element",)
# my_tuple4 = tuple(["Mary", 27, "Rome"])
# print(my_tuple,my_tuple2,my_tuple3,my_tuple4)

# 2. Accessing
# my_tuple = ("John", 21, "Vatican")
# print(my_tuple[1], my_tuple[-3])

# 3. Operations
# my_tuple = ('a','p','p','l','e')
# if 'e' in my_tuple:
#     print('exists')
# print(my_tuple.count('p'))
# print(my_tuple.index('l'))
# print(len(my_tuple))

# 4. Conversions
# my_tuple = (1,2,3,4,5)
# my_list = list(my_tuple)
# my_tuple2 = tuple(my_list)
# print(my_list, my_tuple2)

# 5. SLicing
# my_tuple = (1,2,3,4,5)
# a = my_tuple[0:4]
# b = my_tuple[2:5]
# c = my_tuple[1:5:2]
# d = my_tuple[::-1]
# print(a,b,c,d)

# 6. Unpacking ---> Destructuring
# my_tuple = ('John', 21, 'Paris')
# name, age, city = my_tuple
# print(name, age, city)
#
# my_tuple2 = (1,2,3,4,5,6)
# i1, *i2, i3 = my_tuple2
# print(i1,i2,i3)

