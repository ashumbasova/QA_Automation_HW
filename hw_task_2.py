#HW2_Task_2
l = input("Please provide the line: ")
lenLine = len(l)
if lenLine % 2 == 0:
    i = int(lenLine/2)
else:
    i = lenLine // 2 + 1
print(l[i:] + l[0:i])
