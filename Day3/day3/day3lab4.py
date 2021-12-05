# Given three integers, print the smallest one. (Three integers should be user input)

a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if (a>b & a>c):
    print("a is greatest")
elif (b>a & b>c):
    print("b is greatest")
else:
    print("c is greatest")