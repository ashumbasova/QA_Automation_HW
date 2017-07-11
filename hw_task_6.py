#HW2_Task_6
a = int(input("Please give a= "))
b = int(input("Please give b= "))
c = int(input("Please give c= "))
def triangle (a, b, c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        if a == b == c:
            return "Equilateral triangle"
        elif a == b or b == c or a ==c:
            return "Isosceles triangle"
        else: return "Versatile triangle"
    else: return "Not a triangle"
print(triangle(a, b, c))
