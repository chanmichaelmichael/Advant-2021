import copy
import numpy as np

print("Day 5 Part 1: ")
with open("5-inputs.txt") as f:
    inputs = [line.split("\n")[0] for line in f.readlines()]
    
    #print(inputs)
    coordinates = np.zeros([len(inputs),4]) #x1 y1 x2 y2
    inputs2 = []
    for temp in inputs:
        inputs2.append(temp.split(" -> "))
    for i in range(len(inputs2)):
        coordinates[i,0] = int(inputs2[i][0].split(",")[0])
        coordinates[i,1] = int(inputs2[i][0].split(",")[1])
        coordinates[i,2] = int(inputs2[i][1].split(",")[0])
        coordinates[i,3] = int(inputs2[i][1].split(",")[1])
    
    
    #print(coordinates)
    grid = np.zeros([int(np.max(coordinates))+1,int(np.max(coordinates))+1]) #grid of the vents

    for vent in coordinates:
        if vent[0] == vent[2]: #if columns equal
            #print(vent, "Vertical at ", vent[0])
            y = int(vent[0])
            a = int(min(vent[1],vent[3]))
            b = int(max(vent[1],vent[3]))+1
            for i in range(a,b):
                grid[i,y] = grid[i,y] + 1
            #print(grid)
        elif vent[1] == vent[3]: #if rows equal
            #print(vent, "Horizontal at ", vent[1])
            x = int(vent[1])
            a = int(min(vent[0],vent[2]))
            b = int(max(vent[0],vent[2]))+1
            for i in range(a,b):
                grid[x,i] = grid[x,i] + 1
            #print(grid)
        #else:
        #    print("\tDiagonal")
        
    #print(grid)
    print("Number >= 2's: ", len(grid[grid >= 2]), "\n")

    print("Day 5 Part 2: ")
    grid2 = copy.deepcopy(grid)
    for vent in coordinates:
        if vent[0] != vent[2] and vent[1] != vent[3]: #if diagonal
            if vent[0] > vent[2]:
                pointsBetweenX = [*range(int(vent[0]),int(vent[2])-1,-1)]
            else:
                pointsBetweenX = [*range(int(vent[0]),int(vent[2])+1)]
            if vent[1] > vent[3]:
                pointsBetweenY = [*range(int(vent[1]),int(vent[3])-1,-1)]
            else:
                pointsBetweenY = [*range(int(vent[1]),int(vent[3])+1)]
            for i in range(len(pointsBetweenX)):
                grid2[pointsBetweenY[i],pointsBetweenX[i]] = grid2[pointsBetweenY[i],pointsBetweenX[i]] + 1
            #print("Xs: ", pointsBetweenX) #for testing
            #print("Ys: ", pointsBetweenY) #for testing
    
    #print(grid2) #for testing
    print("Number >= 2's: ", len(grid2[grid2 >= 2]))


