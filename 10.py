import copy
from statistics import median
import time

print("Day 10 Part 1: ")
with open("10-inputs.txt") as f:
    rawInputs = [line.split("\n")[0] for line in f.readlines()]
    
    part1Start = time.time()
    
    #print(rawInputs)
    openBrackets = ["(", "{", "[", "<"]
    closeBrackets = [")", "}", "]", ">"]
    bracketDict = {"(": ")", "{": "}", "[": "]", "<": ">"}
    
    def corruptedPoints(char):
        points = 0
        if char == ")":
            points += 3
        elif char == "]":
            points += 57
        elif char == "}":
            points += 1197
        elif char == ">":
            points += 25137
        return points
            
    
    def findCorruptedLines(inputs):
        output = []
        points = 0
        for line in inputs:
            corrupted = False
            temp = []
            for char in line:
                if char in openBrackets:
                    temp.append(char)
                elif char in closeBrackets:
                    open = temp.pop()
                    #if the close bracket does not fulfil the latest open bracket
                    if open != openBrackets[closeBrackets.index(char)]:
                        corrupted = True
                        points += corruptedPoints(char)
                        break
            if corrupted:
                output.append(line)
        return [output, points]
                
    #print("open bracket test", closeBrackets[openBrackets.index("(")])
    
    #print("corrupted line test:")
    #print(findCorruptedLines(rawInputs))
    
    print("\tScore is: ", findCorruptedLines(rawInputs)[1])
    
    
    part1End = time.time()
    print("\tPart 1 runtime: ", part1Start - part1End, "\n")
    
    
    
    
    
    ##### PART 2 #####
    print("Day 10 Part 2: ")
    part2Start = time.time()
    
    def incompletePoints(tail):
        points = 0
        for i in range(len(tail)):
            char = tail.pop()
            points = points * 5
            if char == "(":
                points += 1
            elif char == "[":
                points += 2
            elif char == "{":
                points += 3
            elif char == "<":
                points += 4
        return points
            
    
    def findIncompleteScores(inputs):
        #output = []
        points = []
        for line in inputs:
            corrupted = False
            temp = []
            for char in line:
                if char in openBrackets:
                    temp.append(char)
                elif char in closeBrackets:
                    open = temp.pop()
                    #if the close bracket does not fulfil the latest open bracket
                    if open != openBrackets[closeBrackets.index(char)]:
                        corrupted = True
                        break
                if corrupted:
                    break
            if not corrupted: #not corrupted equals incomplete
                #print(temp)
                #output.append(temp)
                points.append(incompletePoints(temp))
        return points
    
    scores = findIncompleteScores(rawInputs)
    #print("\tTotal sequence is: ", scores)
    print("\tMedian score is ", median(scores))
    
    part2End = time.time()
    print("\tPart 2 runtime: ", part2Start - part2End, "\n")