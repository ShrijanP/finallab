#Write a Python function to find the Max of three numbers 

def greatervalue(x,y,z):
    if x>y:
        if x>z:

           return x
        else:
         return z
    else:
        if y>x:
            if y>z:
             return y
        else:
             return z

xaa=greatervalue(1,3,2)
print(f"greater value is:{xaa}]")
                

