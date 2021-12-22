#Write a function called fizz_buzz that takes a number.
# If the number is divisible by 3, it should return “Fizz”.
#  If it is divisible by 5, it should return “Buzz”. 
# If it is divisible by both 3 and 5, 
# it should return “FizzBuzz”. Otherwise, it should return the same number. 

def fizz_buzz():
    a=int(input("enter a number"))
    if (a%3==0):
        print("fizz")
    elif (a%5==0):
            print("buzz")
    elif (a%3 and a%5==0):
        print("FizzBuzz")

    else:
        return("a")
fizz_buzz()