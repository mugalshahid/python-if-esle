# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I5b78o6b85ERZ-F1-AjIqBeBASSh0BkZ
"""

age = 18
if(age==18):
  print("my age is 18")

age = 18
if(age==18 or age==19):
  print("my age is 18 or 19")

a = int(input("Enter a age "))
if(10<a<=18):
  print("my is correct")
else:
  print("my is not correct")

a = 10
b = 20
c = 50
if(a < b and a < c):
  print("a is smaller than b and c")

a = 10
b = 14
c = 5
if(a<b and a<c):
  print("a is garib")
elif(b<a and b<c):
  print("b is garib")
else:
  print("c is garib")

num = 19
if(num%2==0):
  print("num is divide by 2")
elif(num%3==0):
  print("num is divide by 3")
elif(num%6==0):
  print("num is divide by 6")
else:
  print("num is not divide by 2,3,6")

a = 19
if(a%2==0 and a%3==0):
  print("a is divisibe by 6")
else:
  print("a is not divisible by 6")

age = 9
if(10<=age<=18):
  print("mature")
elif(18<=age<=30):
  print("young")
elif(30<=age<=60):
  print("old")
else:
  print("age is less")

a = int(input("Enter a number"))
if(a%2==0):
  print("it is a even number")
else:
  print("it is a odd number")

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
if(a>b>c):
  print("largest number of the three")
else:
  print("it is not largest")

year = int(input("Enter first number "))
if(year%4==0 and year%100!=0 or year%400==0):
  print("it is a leap year")
else:
  print("it is a not leap year")

n = int(input("Enter percentage "))
if(n >= 90):
  print("grade A")
elif(n >= 80):
  print("grade B")
elif(n >= 70):
  print("grade C")
elif(n >= 60):
  print("grade D")
elif(n < 60):
  print("grade F")
else:
  print("not matched")

letter = input("Enter alphabet ")
if(letter == 'a or e or o or i or u'):
  print("it is a vowel")
else:
  print("it is a consonant")

a = 34
b = 12
n = input("Enter operator ")
if(n == '+'):
  print("result ",a+b)
elif(n == '-'):
  print("result ",a-b)
elif(n == '*'):
  print("result ",a*b)
elif(n == '/'):
  print("result ",a/b)
else:
  print("operater is not matched")

a = int(input("Enter 1st num"))
b = int(input("Enter 2nd num"))
if(a > 0 and b > 0):
  print("it is positive")
elif(a < 0 and b < 0):
  print("it is negative")
else:
  print("it is zero")

a = input("enter useranme ")
b = input("enter password ")
if(a == 'admin' and b == '1234'):
  print("login successful")
else:
  print("login failed")

a = input("Enter first side ")
b = input("Enter second side ")
c = input("Enter third side ")
if(a + b > c and b + c > a and a + c > b):
  print("a valid triangle")
else:
  print("not valid triangle")

w = int(input("Enter weight "))
h = float(input("Enter height "))
BMI = w/(h**2)
if(BMI < 18.5):
  print("underweight",BMI)
elif(18.5 <= BMI < 24.9):
  print("normal weight",BMI)
elif(25 <= BMI <29.9):
  print("overweight",BMI)
elif(BMI >= 30):
  print("obesity",BMI)
else:
  print("not BMI")

a = int(input("Enter price a product "))
if(a > 1000):
  print("discount of 10%",a-(a*10/100))
elif(500 < a <= 1000):
  print("discount of 5%",a-(a*5/100))
else:
  print("no discount")

age = int(input("Enter the age "))
 if(0 <= age <= 1):
    print("infant")
elif(2 <= age <= 4):
  print("toddler")
elif(5 <= age <= 12):
  print("child")
elif(13 <= age <= 19):
  print("teenager")
elif(20 <= age <= 59):
  print("adult")
elif(age >= 60):
  print("senior")
else:
  print("invalid age")