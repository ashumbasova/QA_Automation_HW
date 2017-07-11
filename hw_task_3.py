#HW2_Task_3
l = "We are not what we should be! We are not what we need to be. But at least we are not what we used to bе " \
    "(Football Coach)"
wordsSum = len(l.split(sep=" "))

newLine = ''
someList = l.split()
for word in someList:
    newLine += word.strip('!,.()') + " "

newList = newLine.split()
newList.sort()

repWords = {}
uniqueList = tuple(newList)
for w in uniqueList:
    counter = 0
    for w2 in newList:
        if w == w2:
            counter += 1
    repWords[w] = counter

print(
    "Provided line was: ", l,
    "Sum of words in provided line: ", wordsSum,
    "Line without punctuation: ", newLine,
    "Sorted words in list: ", newList,
    "Unique list of words: ", repWords,
    sep="\n")

