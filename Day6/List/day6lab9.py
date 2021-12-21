#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements 

'''a=[1,2,3,"shrijan","ok","done","computing"]
a.remove(1)
a.remove("done")
a.remove("computing")
print(a)                    #by using remove function
'''

a=[1,2,3,"shrijan","ok","done","computing","hello"]
del a[0]
del a[4]
del a[5]
print(a)                     #by using del function