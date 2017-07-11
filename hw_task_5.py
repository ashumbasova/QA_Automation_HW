#HW2_Task_5
a = int(input("Please give a= "))
b = int(input("Please give b= "))
c = int(input("Please give c= "))
def isTriangle (a, b, c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
            return True
    else: return False
print(isTriangle(a, b, c))
