#HW2_Task_4
y = int(input("Please enter the year: "))

def isYearLeap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else: return False
print(isYearLeap(y))
