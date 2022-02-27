x = input("Enter x: ")
operator = input("Enter operator: ")
y = input("Enter y: ")

x=int(x)
y=int(y)

if(operator == '+') :
    print(x+y)
elif(operator == '-') :
    print(x-y)
elif(operator == '*') :
    print(x*y)
elif(operator == '/') :
    print(x/y)
elif(operator == '%') :
    print(x%y)
elif(operator == '//') :
    print(x//y)
elif(operator == '**') :
    print(x**y)
else:
    print("Invalid Operator")