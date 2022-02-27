# Input from prompt is always taken as string
x = input("Enter x: ")
y = input("Enter y: ")

# type conversion required to avoid concatenation
print(int(x) + int(y))