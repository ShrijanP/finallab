# Write a Python function that accepts a string and calculate the number of upper case letters 
# and lower case letters.
def up_low(string):
  uppers = 0
  lowers = 0
  for char in string:
    if char.islower():
      lowers += 1
    elif char.isupper():
      uppers +=1
    else:
      pass
  return(uppers, lowers)

print(up_low('hello shrijan?'))
