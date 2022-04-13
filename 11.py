import copy
from itertools import count
import time
import numpy as np

print("Day 11 Part 1: ")
with open("11-inputs-test.txt") as f:
    ### turn inputs into 2d array
    rawInputs = [line.split("\n")[0] for line in f.readlines()]
    
    part1Start = time.time()
    #print(rawInputs)
    
    inputs = []
    for line in rawInputs:
        inputs.append([int(char) for char in line])
    
    inputsArray = np.array(inputs)
    print(inputsArray, "\n")
    
    lastRow = len(inputsArray) - 1
    lastColumn = len(inputsArray[0]) - 1
    
    numRows = len(inputsArray)
    numColumns = len(inputsArray[0])
    
    
    
    ### loops?
    numLoops = 2 #test with 10 loops first 
    flashes = 0 #output
    group = copy.deepcopy(inputsArray)
    
    
    
    
    def relativePos(num):
        if num == 1:
            return "[x-1,y-1]"
        elif num == 2:
            return "[x-1,y]" #2
        elif num == 3:
            return "[x-1,y-1]" #3
        elif num == 4:
            return "[x,y-1]" #4
        elif num == 5:
            return "[x,y+1]" #5
        elif num == 6:
            return "[x+1,y-1]" #6
        elif num == 7:
            return "[x+1,y] #7"
        elif num == 8:
            return "[x+1,y+1]" #8
        else:
            return "error"
    
    #returns a list of coordinates for neighbors
    """
    1 2 3
    4   5
    6 7 8
    """
    def neighbors(x, y):
        output = []
        if x == 0 and y == 0: #top left corner
            output.append([x,y+1]) #5
            output.append([x+1,y]) #7
            output.append([x+1,y+1]) #8
        elif x == 0 and y == lastColumn: #top right corner
            output.append([x,y-1]) #4
            output.append([x+1,y-1]) #6
            output.append([x+1,y]) #7
        elif x == lastRow and y == 0: #bottom left corner
            output.append([x-1,y]) #2
            output.append([x-1,y+1]) #3
            output.append([x,y+1]) #5
        elif x == lastRow and y == lastColumn: #bottom right corner
            output.append([x-1,y-1]) #1
            output.append([x-1,y]) #2
            output.append([x,y-1]) #4
        elif x == 0: #top row middle
            output.append([x,y-1]) #4
            output.append([x,y+1]) #5
            output.append([x+1,y-1]) #6
            output.append([x+1,y]) #7
            output.append([x+1,y+1]) #8
        elif y == 0: #left side
            output.append([x-1,y]) #2
            output.append([x-1,y+1]) #3
            output.append([x,y+1]) #5
            output.append([x+1,y]) #7
            output.append([x+1,y+1]) #8
        elif x == lastRow: #bottom
            output.append([x-1,y-1]) #1
            output.append([x-1,y]) #2
            output.append([x-1,y+1]) #3
            output.append([x,y-1]) #4
            output.append([x,y+1]) #5
        elif y == lastColumn: #right
            output.append([x-1,y-1]) #1
            output.append([x-1,y]) #2
            output.append([x,y-1]) #4
            output.append([x+1,y-1]) #6
            output.append([x+1,y]) #7
        else: #everything in the center
            output.append([x-1,y-1]) #1
            output.append([x-1,y]) #2
            output.append([x-1,y+1]) #3
            output.append([x,y-1]) #4
            output.append([x,y+1]) #5
            output.append([x+1,y-1]) #6
            output.append([x+1,y]) #7
            output.append([x+1,y+1]) #8
        return output
    
    
    ### flash adjacent octopus
    def flashAdj(i, j):
        adj = neighbors(i, j)
        for neighbor in adj:
            #already flashed
            if group[neighbor[0], neighbor[1]] == 0: 
                return 0
            #going to flash
            elif group[neighbor[0], neighbor[1]] == 9: 
                temp = 1
                group[neighbor[0], neighbor[1]] = 0
                temp += flashAdj(neighbor[0], neighbor[1])
                return temp
            #nothing
            else: 
                group[neighbor[0], neighbor[1]] = group[neighbor[0], neighbor[1]] + 1
                return 0
    
    ### MAIN FUNCTION
    for loop in range(numLoops):
        print("Step ", loop)
        ###first, energy level of all octopus increases by 1
        group = group + 1
        #print("Number of add'l flashes: ", len(group[group == 10])) 
        #flashes += len(group[group == 10]) #initial flash
        
        ###all the ones whose neighbors we need to affect
        flashers = np.where(np.isin(group, 10))
        
        flashes += len(flashers[0]) #initial flash
        group[flashers] = 0
        
        print("x: ", flashers[0])
        print("y: ", flashers[1])
        
        for i in range(len(flashers[0])):
            #x is flashers[0][i]
            #y is flashers[1][i]
            flashes = flashes + flashAdj(flashers[0][i], flashers[1][i])
        
        """
        #REMEMBER TO CHANGE ALL 10s to 0s at the end        
        print("pre reset to 0: ", group, "\n")
        group[group == 10] = 0
        print("post reset to 0: ", group, "\n\n")
        """
        
        print("Total Flashes: ", flashes)        
        print(group, "\n")
    
    print("Final Group")
    print(group, "\n")
    #print("x: ", flashers[0][0])
    #print("y: ", flashers[1][0])
    
    
    
    part1End = time.time()
    print("\tPart 1 runtime: ", part1Start - part1End, "\n")
    
    
    ##### PART 2 #####
    print("Day 11 Part 2: ")
    part2Start = time.time()
    
    
    part2End = time.time()
    print("\tPart 2 runtime: ", part2Start - part2End, "\n")