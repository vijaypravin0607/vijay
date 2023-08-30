"""# 1. Python Program to Print Hello world!
print("Hello,world!")

# 2. Python Program to Add Two Numbers
a=2
b=20
print("Total :",a+b)

# 3. Python Program to Find the Square Root
a=int(input("Enter the Squre root mumber :"))
print("The",a,"Squre root value :",a**0.5)

# 4.Python Program to Calculate the Area of a Triangle
length=int(input("Enter the length value:"))
width=int(input("Enter the width value:"))
area=(length*width)
print("Area of triangle : ",area)

# 5.Python Program to Solve Quadratic Equation
import cmath
a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))

# 6.Python Program to Swap Two Variables
a=20
b=30
temp=b
b=a
a=temp
print(a,b)

# 7.Python Program to Generate a Random Number
import random
print(random.randint(0,100))

# 8. Python Program to Convert Kilometers to Miles
a=int(input("Enter the value :"))
b=a*0.621371
print(a,"convert to miles value :",b)

# 9. Python Program to Convert Celsius To Fahrenheit
a=int(input("Enter the celsius value :"))
b=(a)*(9/5)+32
print(a,"celsius to Fahrenheit vslue is :",b)

# 10.Python Program to Check if a Number is Positive, Negative or 0
num=int(input("Enter the value :"))
if num==0:
    print("Zero")
elif num>0:
    print(num,"is Positive Number ")
else:
    print(num,"is Negative Number ")

# 11.Python Program to Check if a Number is Odd or Even
num=int(input("Enter the value :"))
if num%2==0:
    print(num,"is Even number")
else:
    print(num,"is odd number")

# 12.Python Program to Check Leap year
year=int(input("Enter the year :"))
if year%400==0 and year%100==0:
    print("This",year,"is leap year")
    if (year % 4 == 0) and (year % 100 != 0):
        print("This",year,"is leap year")
else:
    print("This",year,"is not a leap year")

# 13.Python Program to Find the Largest Among Three Numbers
a=int(input("Enter the a value :"))
b=int(input("Enter the b value :"))
c=int(input("Enter the c value :"))
if a>=b and a>=c:
    print(a,"- is a biggest number")
elif b>=c and b>=a:
        print(b,"- is a biggest number")
else:
    print(c,"- is a biggest number")

# 14.Python Program to Check Prime Number
num = int(input("enter :"))
a = False
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            a = True
            break
    if a:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")"""
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
print (','.join(l))