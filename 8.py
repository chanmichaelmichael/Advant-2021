import copy
import numpy as np
import time
import difflib

print("Day 8 Part 1: ")
with open("8-inputs.txt") as f:
    rawInputs = [line.split("\n")[0] for line in f.readlines()]
    
    #each line is jumbled up in different ways
    patternRaw = [line.split(" | ")[0].split(" ") for line in rawInputs]
    outputRaw = [line.split(" | ")[1].split(" ") for line in rawInputs]
    
    part1Start = time.time()
    count = 0
    compare = [2, 4, 3, 7] #lengths of 1, 4, 7, 8
    for i in range(len(outputRaw)):
        for j in range(len(outputRaw[i])):
            if len(outputRaw[i][j]) in compare:
                count += 1
    
    print("\t1, 4, 7, 8 appears ", count, " times.")

    part1End = time.time()
    print("\tPart 1 runtime: ", part1Start - part1End, "\n")
    
    
    print("Day 8 Part 2: ")
    part2Start = time.time()
    #print(patternRaw)
    patternRawLengths = [] #length of each string... corresponding to patterns
    for i in range(len(patternRaw)):
        #patternRaw[i] = sorted(patternRaw[i], reverse = True)
        patternRawLengths.append([len(item) for item in patternRaw[i]])
    #print(patternLengths)
    dictionary = [None] * 10
    
    #function to return difference between strings
    def difference(str1, str2):
        changes = [li[-1] for li in difflib.ndiff(str1, str2) if li[0] != ' ']
        test = []
        for i in changes:
            if i in test:
                test.remove(i)
            else: 
                test.append(i)
        return test
    #print("function test: ", difference(dictionary[7], dictionary[1]))
    
    comparison = ["a", "b", "c", "d", "e", "f", "g"]
    outputValues = []
    
    #####first solve it for first line
    for lines in range(len(patternRaw)):
        
        #print(patternRaw[lines])
        #print(patternRawLengths[lines])
        #print("")
        dictionary[1] = patternRaw[lines][patternRawLengths[lines].index(2)]
        dictionary[4] = patternRaw[lines][patternRawLengths[lines].index(4)]
        dictionary[7] = patternRaw[lines][patternRawLengths[lines].index(3)]
        dictionary[8] = patternRaw[lines][patternRawLengths[lines].index(7)]
        #print(dictionary, "\n")
    
        a = difference(dictionary[7], dictionary[1])[0].strip()
        b = ""
        c = ""
        d = ""
        g = ""
        e = ""

        patternRaw[lines] = [x for _,x in sorted(zip(patternRawLengths[lines],patternRaw[lines]), reverse = True)]
        patternRawLengths[lines] = sorted(patternRawLengths[lines], reverse = True)
        for j in range(len(patternRaw[lines])):
            #if length is 6, there are three options [9, 6, 0]
            if len(patternRaw[lines][j]) == 6:
                #print(patternRaw[0][j], " sorts into ", sorted(patternRaw[0][j]))
                #finds c by comparing "1" with  6 length thing without c
                if dictionary[1][0] not in sorted(patternRaw[lines][j]):
                    c = dictionary[1][0]
                if dictionary[1][1] not in sorted(patternRaw[lines][j]):
                    c = dictionary[1][1].strip()
                #print("\tCompare to 4+a: ", set(dictionary[4]+a))
            
                #finds 9, which is the string with 1 more than 4 + a
                if len(difference(dictionary[4]+a, patternRaw[lines][j])) == 1:
                    dictionary[9] = patternRaw[lines][j]
                    g = difference(dictionary[4]+a, dictionary[9])[0].strip()
                    e = difference(dictionary[8], dictionary[9])[0].strip()
                # 6 is 8 minus c
                elif sorted(patternRaw[lines][j]) == sorted(dictionary[8].replace(c, "")):
                    dictionary[6] = patternRaw[lines][j] #found what 6 is
                #otherwise it is a 0
                else:
                    dictionary[0] = patternRaw[lines][j]
                #print(dictionary[1][0], " in ", patternRaw[0][j], "? ", dictionary[1][0] in sorted(patternRaw[0][j]))
                #print(dictionary[1][1], " in ", patternRaw[0][j], "? ", dictionary[1][1] in sorted(patternRaw[0][j]))
            #length 5, which is [2, 3, 5]
            #elif len(patternRaw[0][j]) == 5:
                #3 and 5 are 1 away from 9
                #3 and 2 have 1 unknown
        f = difference(dictionary[1], c)[0].strip()
        d = difference(dictionary[8], dictionary[0])[0].strip()
        #print("d ", difference(dictionary[8], dictionary[0]))
    
        tempComp = copy.deepcopy(comparison)
        tempComp.remove(a)
        tempComp.remove(c)
        tempComp.remove(d)
        tempComp.remove(e)
        tempComp.remove(f)
        tempComp.remove(g)
        b = tempComp[0]
    
        dictionary[2] = a+c+d+e+g
        dictionary[3] = a+c+d+f+g
        dictionary[5] = a+b+d+f+g
    
        #print(outputRaw[0])
        
        """
        print("a is ", a)
        print("b is ", b)
        print("c is ", c)
        print("d is ", d)
        print("e is ", e)
        print("f is ", f)
        print("g is ", g)
        """
  
    
        #print("4 + a: ", dictionary[4]+a)
    
        #print(dictionary[8].replace(c, ""))
    
        #print(patternRaw[0])
        #print(patternRawLengths[0])
        #print("sort")
        #print([x for _,x in sorted(zip(patternRawLengths[0],patternRaw[0]))])
        #print(sorted(patternRawLengths[0]))
    
        #print("dictionary so far: ", dictionary)
    
        #TIME TO READ THE OUTPUTS!
        outputValue = ""
        for output in outputRaw[lines]:
            for i in range(len(dictionary)):
                if sorted(output) == sorted(dictionary[i]):
                    outputValue = outputValue + str(i)
        #print("OutputValue: ", outputValue)
        outputValues.append(int(outputValue))
    
        #print("OutputValues: ", outputValues)
    print("\tTotal of output values is: ", sum(outputValues))

    part2End = time.time()
    print("\tPart 2 runtime: ", part2Start - part2End, "\n")