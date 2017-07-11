#HW2_Task_7
import math
x1 = float(input("Please enter int x1: "))
y1 = float(input("Please enter int y1: "))
x2 = float(input("Please enter int x2: "))
y2 = float(input("Please enter int y2: "))

def distance(x1, y1, x2, y2):
       return(math.sqrt(math.pow((x1-x2), 2) + math.pow((y1-y2), 2)))
print(distance(x1, y1, x2, y2))
