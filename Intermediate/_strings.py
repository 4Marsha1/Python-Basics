# STRING : Ordered, immutable, used for text representation

# 1. Declaration
# myStr = "hello"
# myStr2 = 'I\'m a boy'
# myStr3 = """
#     MULTI LINE STRING
#         IT ALSO KEEPS THE INDENTATION
#             ISN'T THAT COOL!
# """
# print(myStr, myStr2)
# print(myStr3)

# 2. Access
# myStr = "hello world"
# print(myStr[2], myStr[-5])

# 3. SLICING
# substring = myStr[2::2]
# print(substring)

# 4.----- OPERATIONS---
# CONCATENATION
# str1 = "hello"
# str2 = 'world'
# new_str = str1 + str2
# print(new_str)

# REMOVE WHITE SPACE
# str = "         WOW SO MUCH SPACE          "
# print(str)
# new_str = str.strip()
# print(new_str)

# UPPER & LOWER
# str = 'abcdefghi'
# upper = str.upper()
# print(upper)
# lower = upper.lower()
# print(lower)

# STARTSWITH & ENDSWITH
# str = 'hello world'
# print(str.startswith('h'))
# print(str.startswith('hel'))
# print(str.endswith('d'))
# print(str.endswith('world'))

# FIND & COUNT
# str = 'abcudgaghagjfds'
# print(str.find('f'))        # returns INDEX
# print(str.count('g'))       # returns COUNT

# REPLACE
# str = 'hello world'
# new_str = str.replace('world', 'duniya!')
# print(str, new_str)

# SPLIT & JOIN
# str = 'hey ! how are your doing bro ?'
# new_list = str.split(' ')
# print(str)
# print(new_list)

# new_str = ' '.join(new_list)
# print(new_str)


# 5. STRING FORMATTING
# name = "John"
# age = 21
# salary = 400.24565474

# A. ---------- using %
# str = "I am %s, I am %d years old, I earn %f monthly" % (name, age, salary)
# print(str)

# B. ---------- using .format()
# str = "I am {}, I am {} years old! I earn {:.4f} monthly".format(name, age, salary)
# print(str)

# C. --------- using f-Strings
# str = f"I am {name}. I am {age} years old! I earn {salary} monthly"
# print(str)