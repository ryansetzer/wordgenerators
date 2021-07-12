import random

file = open("combinations.txt", "r")
combinations = []
for line in range(1, 8):
    currentLine = file.readlines(line)
    tempArray = currentLine.split('')
    tempArray.append(tempArray)
    print(currentLine)
print(combinations)