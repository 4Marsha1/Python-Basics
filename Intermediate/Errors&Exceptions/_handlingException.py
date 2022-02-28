# SIMPLE try-except
# try:
#     a = 5/0
# except Exception as e:
#     print(e)


# SPECIFIC try-except
# try:
#     a = 5/1
#     b = a + "10"
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)

# FULL FLEDGED try-except
try:
    a = 5/1
    b = a + 19
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('Everything worked fine!')
finally:
    print("Cleaning up...")