#find BMI of a person where take mass and height as input from the user
#bmi=mass in kg/(height in m)^2


m = int(input("enter the mass of person in kg:"))
h =float(input("enter the height of a person in meter:"))
BMI =(m/ (h * h))
print(f"the bmi value of a person is {BMI}")