# LISTS: Ordered, Mutable, allows Duplicate elements

# 1. Declaration
# myList = [18, "age", True, 18]
# print(myList)

# myList2 = list()
# print(myList2)

# 2. Accessing
# myList = [1,6,8,2,3,4]
# print(myList[0], myList[-2])

# 3. Operations
# myList.append(10)
# myList.insert(3,20)
# print(myList)
# print(len(myList))
# item = myList.pop()
# print(item)
# print(myList)
# myList.remove(8)
# print(myList)
# myList.clear()
# print(myList)

# myList.reverse()
# print(myList)
# myList.sort()
# print(myList)

# new_list = sorted(myList)
# print(new_list)

# 4. Concatenation
# myList = [2]*5
# print(myList)
# myList2 = [1,2,3,4,6]
# print(myList2)
# new_list = myList + myList2
# print(new_list)

# 5. Slicing --> (start,end,step)
# myList = [1,2,3,4,5]
# a = myList[0:3]
# b = myList[0:4:1]
# c = myList[::-1]
# d = myList[:4:2]
# print(a,b,c,d)

# 6. Copying
# myList = [1,2,3,4,5]
# myList_copy = myList        # Both points to same list now
# myList_copy.append(13)      # Any changes in One, Cause changes in other
# print(myList, myList_copy)

# myList = [1,2,3,4,5]
# myList_copy = myList.copy()   # 1 Way (.copy())
# myList_copy = list(myList)    # 2 Way (create new instance)
# myList_copy = myList[:]       # 3 Way (Slicing from 0 to n)
# myList_copy.append(13)
# print(myList,myList_copy)

# 7. List Comprehension  ---> [expression   for loop on list]
# myList = [1,2,3,4,5]
# myList_squared = [i*i for i in myList]
# myList_copy = [i for i in myList]
# print(myList)
# print(myList_squared)
# print(myList_copy)