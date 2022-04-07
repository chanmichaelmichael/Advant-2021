import copy
import time

print("Day 9 Part 1: ")
with open("9-inputs.txt") as f:
    rawInputs = [line.split("\n")[0] for line in f.readlines()]
    
    part1Start = time.time()
    
    numRows = len(rawInputs)
    numColumns = len(rawInputs[0])
    print("NumRows: ", numRows)
    print("NumColumns: ", numColumns)
    
    lastRow = numRows - 1
    lastColumn = numColumns - 1
    
    lowPoints = []
    lowPointsX = []
    lowPointsY = []
    
    #probably unneeded but checks column size uniformity
    for i in range(numRows):
        if len(rawInputs[i]) != numColumns:
            print("Column size not unifform on row ", i)
            break
    
    #center
    for i in range(1, numRows-1):
        for j in range(1, numColumns-1):
            this = rawInputs[i][j]
            if this < min(rawInputs[i-1][j], rawInputs[i][j-1], rawInputs[i+1][j], rawInputs[i][j+1]):
                lowPoints.append(int(this))
                lowPointsX.append(i)
                lowPointsY.append(j)
    
    #first column
    for i in range(numRows):
        this = rawInputs[i][0]
        if i == 0: #top left corner
            #print("top left corner i ", i, " and j ", 0)
            if this < min(rawInputs[0][1], rawInputs[1][0]):
                lowPoints.append(int(this))
                lowPointsX.append(i)
                lowPointsY.append(0)
        elif i == lastRow: #bottom left corner
            #print("bottom left corner i ", i, " and j ", 0)
            if this < min(rawInputs[i-1][0], rawInputs[i][1]):
                lowPoints.append(int(this))
                lowPointsX.append(i)
                lowPointsY.append(0)
        else: #middle first column
            #print("first column i ", i, " and j ", 0)
            if this < min(rawInputs[i-1][0], rawInputs[i+1][0], rawInputs[i][1]):
                lowPoints.append(int(this))
                lowPointsX.append(i)
                lowPointsY.append(0)
    
    #last column
    for i in range(numRows):
        this = rawInputs[i][lastColumn]
        if i == 0: #top right corner
            #print("top right corner i ", i, " and j ", numColumns)
            if this < min(rawInputs[i][lastColumn-1], rawInputs[i-1][lastColumn]):
                lowPoints.append(int(this))
                lowPointsX.append(i)
                lowPointsY.append(lastColumn)
        elif i == numRows-1: #bottom right corner
            #print("bottom right corner i ", i, " and j ", numColumns)
            if this < min(rawInputs[i][lastColumn-1], rawInputs[i-1][lastColumn]):
                lowPoints.append(int(this))
                lowPointsX.append(i)
                lowPointsY.append(lastColumn)
        else:
            #print("last column i ", i, " and j ", numColumns)
            if this < min(rawInputs[i-1][lastColumn], rawInputs[i+1][lastColumn], rawInputs[i][lastColumn-1]):
                lowPoints.append(int(this))
                lowPointsX.append(i)
                lowPointsY.append(lastColumn)
            
    #first row
    for j in range(numColumns):
        this = rawInputs[0][j]
        if j == 0: #top left corner
            #print("top left corner i ", 0, " and j ", j, " SKIPPED")
            continue
        elif j == numColumns-1: #top right corner
            #print("top right corner i ", 0, " and j ", j, " SKIPPED")
            continue
            if this < min(rawInputs[0][j-1], rawInputs[0][j]):
                lowPoints.append(this)
        else: #middle top row
            #print("top row i ", 0, " and j ", j)
            if this < min(rawInputs[1][j], rawInputs[0][j-1], rawInputs[0][j+1]):
                lowPoints.append(int(this))
                lowPointsX.append(0)
                lowPointsY.append(j)
    
    #last row
    for j in range(numColumns):
        this = rawInputs[lastRow][j]
        if j == 0: #bottom left corner
            continue
        elif j == lastColumn: #bottom right corner
            continue
            if this < min(rawInputs[lastRow-1][j], rawInputs[lastRow][j-1]):
                lowPoints.append(this)
        else:
            #print("last row i ", numRows-1, " and j ", j)
            if this < min(rawInputs[lastRow-1][j], rawInputs[lastRow][j-1], rawInputs[lastRow][j+1]):
                lowPoints.append(int(this))
                lowPointsX.append(lastRow)
                lowPointsY.append(j)
    
    
    #print(rawInputs)
    #print(rawInputs[0])
    #print(rawInputs[0][0])
    
    riskLevel = []
    print("Low Points: ", lowPoints)
    
    for pt in lowPoints:
        riskLevel.append(pt+1)
    
    print("Risk Level: ", riskLevel)
    print("Total Risk: ", sum(riskLevel))
    
    part1End = time.time()
    print("\tPart 1 runtime: ", part1Start - part1End, "\n")
    
    
    ##### PART 2 #####
    print("Day 9 Part 2: ")
    part2Start = time.time()
    #print("Low  X's: ", lowPointsX)
    #print("Low Y's: ", lowPointsY)
    
    
    #returns a list of coordinates for neighbors
    def neighbors(x, y):
        output = []
        if x == 0 and y == 0:
            output.append([1,0])
            output.append([0,1])
        elif x == 0 and y == lastColumn:
            output.append([1,lastColumn])
            output.append([0,lastColumn-1])
        elif x == lastRow and y == 0:
            output.append([lastRow-1,0])
            output.append([lastRow,1])
        elif x == lastRow and y == lastColumn:
            output.append([lastRow-1,lastColumn])
            output.append([lastRow,lastColumn-1])
        elif x == 0:
            output.append([x+1,y])
            output.append([x,y+1])
            output.append([x,y-1])
        elif y == 0:
            output.append([x+1,y])
            output.append([x-1,y])
            output.append([x,y+1])
        elif x == lastRow:
            output.append([x-1,y])
            output.append([x,y+1])
            output.append([x,y-1])
        elif y == lastColumn:
            output.append([x+1,y])
            output.append([x-1,y])
            output.append([x,y-1])
        else: #everything in the center
            output.append([x+1,y])
            output.append([x-1,y])
            output.append([x,y+1])
            output.append([x,y-1])
        return output
    
    
    #input is a low point
    def findBasinSize(x, y):
        #print(f"checking {x} and {y}, height is {rawInputs[x][y]}")
        if int(rawInputs[x][y]) == 9:
            #print(f"\thit a wall at x:{x} and y:{y}")
            return 0
        elif [x, y] in traversed:
            return 0
        else:
            #print("already traversed ", traversed)
            #print("traversing ", x, " and ", y)
            temp = 1
            traversed.append([x,y])
            for neighbor in neighbors(x, y):
                temp += findBasinSize(neighbor[0], neighbor[1])
            return temp
    
    
    
    
    
    #test = []
    #test.append([1,0])
    #test.append([0,1])
    #print(test[1][1])

    #print("neighbors test:")
    #test = neighbors(0, 1)
    #print(test)
    #for neighbor in test:
    #    print(neighbor[0])
    #    print(neighbor[1])
    #print([2, 1] in test)
    
    #print("find basin test: ")
    #traversed = []
    #print("\tbasin size is: ", findBasinSize(0, 1))
    
    #for each low point on the map, find the size of the basin around it
    basinSizes = []
    for i in range(len(lowPointsX)):
        traversed = []
        basinSizes.append(findBasinSize(lowPointsX[i], lowPointsY[i]))
    basinSizes = sorted(basinSizes, reverse = True)
    
    print("3 largest basin sizes are: ", sorted(basinSizes, reverse = True)[:3])
    print("product of 3 largest basin sizes are: ", basinSizes[0]*basinSizes[1]*basinSizes[2])
    
    
    
    
    part2End = time.time()
    print("\tPart 2 runtime: ", part2Start - part2End, "\n")