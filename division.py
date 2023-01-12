import math
a = int(input("enter the first number : "))
b = int(input("enter the second number :  "))
c = str(input("enter the value : "))
d =a/b
if c=="ceil":
    print(math.ceil(d))
elif c=="floor":
    print(math.floor(d))
else:
    print(d)
