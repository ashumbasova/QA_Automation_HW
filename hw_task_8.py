#HW2_Task_8

def function(*nums):
    unique = tuple(nums)
    uniqueList = list(unique)
    uniqueList.sort()
    return uniqueList[1]

print(function(55,66,77,88,44,55,66))
