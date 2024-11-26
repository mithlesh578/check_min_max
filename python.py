import math
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
a = int(input("Enter 1 to check max and enter 2 to check min: "))
if a==1:
    def max():
        m = max(x,y,z)
        print("maximum is :",m)
    max()
elif a==2:
    def min():
        n = min(x,y,z)
        print("minimum is :",n)
    min()
else:
    print("Invalid Input!")