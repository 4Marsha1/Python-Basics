# COLLECTIONS: Counter, namedtuple, OrderedDict, defaultdict, deque

# 1. Counter
# from collections import Counter
# str = "aaabbbbccccddeefgh"
# myCounter = Counter(str)
# print(myCounter)

# ------------- OPERATIONS
# myCounter_items = myCounter.items()
# print(myCounter_items)
# myCounter_keys = myCounter.keys()
# print(myCounter_keys)
# myCounter_values = myCounter.values()
# print(myCounter_values)

# myCounter_common = myCounter.most_common(1)
# print(myCounter_common)
# myCounter_common_key = myCounter.most_common(1)[0][0]
# print(myCounter_common_key)

# my_list = list(myCounter.elements())
# print(my_list)

# 2. namedtuple
# from collections import namedtuple
# Point = namedtuple('Point', 'x,y,z')
# pt = Point(1,5,-10)
# print(pt)
# print(pt.x)
# print(pt.y)
# print(pt.z)

# Student = namedtuple('Student', 'name, age, address')
# student = Student('John', 19, 'Paris')
# print(student)

# 3. OrderedDict
# from collections import OrderedDict
# ordered_dict = OrderedDict()
# ordered_dict['a'] = 1
# ordered_dict['b'] = 2
# ordered_dict['c'] = 10
# print(ordered_dict)

# 4. defaultdict
# from collections import defaultdict
# dict = defaultdict(int)
# dict = defaultdict(float)
# dict['a'] = 2
# dict['b'] = 10
# print(dict['a'])
# print(dict['h'])

# 5. deque
# from collections import deque
# d = deque()

# ----------- OPERATIONS
# FROM RIGHT
# d.append(1)
# d.append(2)
# d.pop()
# d.extend([4,5,6])
# d.rotate(2)
# print(d)

# FROM LEFT
# d.appendleft(10)
# d.popleft()
# d.extendleft([11,12,13])
# d.rotate(-1)
# print(d)

# d.clear()
# print(d)