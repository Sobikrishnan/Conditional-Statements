"""Example

y = 54
if y > 10:
    print("y is greater than 10")
    if y < 100:
     print("y is smaller than 100")
print ("All done")

age = int(input("Please enter your age: "))

if age >= 18:
    print("You are allowed")
else :
    print("You are not allowed")
print("Have a good day")"""

"""Activity 1
num = int(input("Enter a number: "))

if num > 0:
    print("This is positive number")
elif num < 0:
    print("This is negative number")
else :
    print("This is a 0 value")"""

"""Activity 2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

"if (num1 == num2) and (num2 == num3):"
if num1 == num2 == num3:
    print("Equal")
else :
    print("Not Equal")"""

"""Activity 3

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 > num2) and (num1 > num3):
    print("The maximum number is:", num1)
elif (num2 > num3) and (num2 > num1):
    print("The maximum number is:", num2)
else:
    print("The maximum number is:", num3)"""

"""Activity 4

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if (num1 < num2) and (num1 < num3):
    print("The minimum number is:", num1)
elif (num2 < num3) and (num2 < num1):
    print("The minimum number is:", num2)
else:
    print("The minimum number is:", num3)"""

"""Activity 5

weight = float(input("Please enter weight: "))
unit = input("Enter unit type kg/lb: ")

if (unit == 'kg'):
    n = weight*2.20
    print(weight,"kg to pounds =",n,"lb")

if (unit == 'lb'):
    m = weight/2.20
    print(weight,"lb to pounds =",m,"kg")"""

"""Activity 6

num1 = float(input("Enter first number: "))
operator = input("Enter the operator (+-*/): ")
num2 = float(input("Enter third number: "))

if operator == "+":
    result = num1+num2
    print(result)
elif operator == "-":
    result = num1-num2
    print(result)
elif operator == "*":
    result = num1*num2
    print(result)
elif operator == "/":
    result = num1/num2
    print(result)
else:
    print("Please enter a valid operator within (+-*/)")"""

"""Example if elif else

marks = int(input("Enter your marks:"))

if marks >= 75:
    print("You got an 'A'")
elif marks >= 65:
    print("You got a 'B'")
elif marks >= 50:
    print("You got a 'C'")
elif marks >= 35:
    print("You got a 'S'")
else:
    print("You got a 'W'")"""

"""Activity 7

# modulus
# integer division
# O division error

num1 = float(input("Enter first number: "))
operator = input("Enter the operator (+,-,*,/,//,%): ")
num2 = float(input("Enter third number: "))

if operator == "+":
    result = num1+num2
    print(result)
elif operator == "-":
    result = num1-num2
    print(result)
elif operator == "*":
    result = num1*num2
    print(result)
elif operator == "/":
    if num2 == 0:
        print("Please enter a number without 0")
    else:
         result = num1/num2
         print(result)
elif operator == "//":
    if num2 == 0:
        print("Please enter a number without 0")
    else:
        result = int(num1/num2)
        print(result)
elif operator == "%":
    if num2 == 0:
        print("Please enter a number without 0")
    else:
        result = int(num1%num2)
        print(result)
else:
    print("Please enter a valid operator within (+,-,*,/,//,%)")"""

"""Activity 8

# check the password has 'at least 8 characters'
# check the password contains '#'

password = "cpwKZ12#ga"
if "#" in password and len(password) >= 8 :
    print("Password Correct")
else:
    print("Password Incorrect")"""

"""Activity 9

unit = input("Enter temperature unit (C/F): ")
value = float(input("Enter temperature value: "))

if unit == "C" or unit == "c":
    result = (value*9)/5+32
    print(result,"°F")
if unit == "F" or unit == "f":
    result = (value-32)*5/9
    print(result,"°C")"""

"""random module

import random

print(random.random())

print(random.randint(1,5))

number = [1,2,3,4,5,6,7,8,9]
x = random.choice(number)
print(x)

x = random.choices(number, k=3)
print(x)

random.shuffle(number)
print(number)"""

"""Activity 10"""

import random

computer = random.randint(0,1)

user = int(input("Enter Tail(0) or Head(1): "))

if user>1 or user<0:
    print("Please enter 0 or 1")
elif user == computer:
    print("You won 🎉🎉🎉")
else:
    print("Better luck next time 😉😉")

#result = ["Head", "Tail"]
#x = random.choice(result)
#print(x)