# Saying 'Hi!"

x = input("Say Hi to me: ")
if x.upper() == "HI":
    print("Hello")
else: print("I've asked for 'Hi'")

# Even or odd numbers
x = input("Please enter number x, where 0 < x <= 100: ")
if 0 < int(x) <= 100:
    print("Correct number")
else: print("Incorrect number")

#Verificate the line: number / text / mixed
x = input("Please enter here text or number: ")
if x.isdigit():
    print(x, "is number")
elif x.isalpha():
    print(x, "is text")
else: print(x, "has both numbers and text")


# # Count of special symbols in line
x = input("Enter the line with spaces: ")
z = x.count(" ")
print(z, "is number of spaces in line")

# Filling space with requested symbols for both sides of input
l = input("Please enter word Homework: ")
middle_index = len(l) // 2

first_half = l[0:middle_index].rjust(50, ' ')
second_half = l[middle_index:].ljust(50, ' ')
print(first_half + second_half)

# Upper case for all words in line
l = input("Enter a sentence: ")
print(l.title())

# Gipotenuza 179 and 971 a2 + b2 = c2, c=sqrt(x)

import math

print("need to calculate sqrt(x) if a = 179 and b = 971: ")
a = 179
b = 971
x = math.sqrt(a * a + b * b)
print(x)

x = input("Enter two digits integer number between 10 and 99: ")
try:
    if 10 <= int(x) and int(x) <= 99:
        z = int(x) // 10
        print(z)
    else: print("Your number is not between 10 and 99 ")
except:
    print("Not integer number between 10 and 99")

x = input("Enter three digits integer number between 100 and 999: ")
try:
    if 100 <= int(x) and int(x) <= 999:
        z = int(x[0]) + int(x[1]) + int(x[2])
        print(z)
    else: print("Your number is not between 100 and 999")
except:
    print("Not integer number between 100 and 999")

x = input("Enter integer number: ")
try:
    if int(x) % 2 == 0:
        print(int(x) + 2, "is next even number")
    else: print(int(x)+1, "is next even number")
except:
    print("Not integer number")

y = input("Please enter year: ")
try:
    year = int(y)
    if year % 400 == 0:
        print(year, "Yes")
    elif year % 4 == 0 and year % 100 != 0:
        print(y, "Yes")
    else: print(y, "No")
except:
    print('is not a year')

a = input("Please give a= ")
b = input("Please give b= ")
c = input("Please give c= ")
try:
    A = int(a)
    B = int(b)
    C = int(c)
    if (A + B) > C and (B + C) > A and (A + C) > B:
        print("Yes")
    else: print("No")
except:
    print("Not valid data. Only int numbers should be provided")

a = input("Please give a= ")
b = input("Please give b= ")
c = input("Please give c= ")
try:
    A = int(a)
    B = int(b)
    C = int(c)
    if A > B:
        (A,B) = (B,A)
    if B > C:
        (B, C) = (C, B)
    if A > B:
        (A,B) = (B,A)
    print("a=", A, "b=", B, "c=", C)
except:
    print("Not valid data. Only int numbers should be provided")


a = input("Please give a= ")
b = input("Please give b= ")
c = input("Please give c= ")
try:
    A = int(a)
    B = int(b)
    C = int(c)
    if A == B == C:
        print("3")
    elif A == B or B == C or A == C:
        print("2")
    else: print("0")
except:
    print("Not valid data. Only int numbers should be provided")

# While-for_task
x = input("Please enter 1 if you want to count from 0 to 10 or 2 if you want count from 20 to 1: ")

try:
    choice = int(x)
    if choice == 1:
        x = 0
        while x <=10:
            print(x)
            x += 1
    elif choice == 2:
        x = 20
        while x >= 1:
            print(x)
            x -= 1
    else:
        print("Incorrect input. Only 1 or 2 should be selected")
except:
    print("Only 1 or 2 should be selected")

# 8
l = ['aaaaaa', 'fjgkbkbkb', "fgkhlhl", "jvvkvk"]
l.sort()
print(l)
while l:
    first = l.pop(0)
    print("-", first)
    print(l)

