# DICTIONARY: Unordered, mutable, Key-Value Pairs

# 1. Declaration
# mydict = {"name": "John", "age": 21, "city": "Paris"}
# print(mydict)
# mydict2 = dict(name="Mary", age=24, city="Rome")
# print(mydict2)

# 2. Access
# mydict = {"name": "John", "age": 21, "city": "Paris"}
# print(mydict["name"])

# 3. Update OR Add New
# mydict['email'] = 'ab@gmail.com'
# mydict['age'] = 22
# print(mydict)

# 4. Delete
# del mydict['email']
# mydict.pop('email')
# mydict.popitem()
# print(mydict)

# 5. OPERATIONS
# if "city" in mydict:
#     print(mydict["city"])

# ---- try-except Method ----
# try:
#     print(mydict["age"])
# except:
#     print("error!")

# 6. Looping
# print("----PRINTING KEYS ONLY----")
# for key in mydict.keys():
#     print(key)
# print("----PRINTING VALUES ONLY----")
# for value in mydict.values():
#     print(value)
# print("----PRINTING KEY-VALUE----")
# for key,value in mydict.items():
#     print(key,value)

# 7. Copying
# mydict = {"name": "John", "age": 21, "city": "Paris"}
# mydict2 = mydict.copy()       # 1 Way: .copy() Method
# mydict2 = dict(mydict)        # 2 Way: dict() to create a new instance
# print(mydict, mydict2)

# 8. Merging
# mydict = {"name": "John", "age": 21, "city": "Paris"}
# mydict2 = {"name": "Mary", "email": "ab@gmail.com"}
# mydict.update(mydict2)
# print(mydict)

# 9. Tuple as key ---------> Keys should be immutable
# mytuple = (10,9)
# mydict = {mytuple: 19}
# print(mydict)