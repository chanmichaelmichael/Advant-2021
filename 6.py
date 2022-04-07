import copy
import numpy as np
import time

with open("6-inputs.txt") as f:
    part1Start = time.time()
    print("Day 6 Part 1: ")
    ### inputs = list(map(int, f.readlines()[0].split(",")))
    init = [int(i) for i in f.readlines()[0].split(",")] #list comprehension
    school = copy.deepcopy(init)
    #print("Initial state: ", school)
    duration = 80 #days

    for i in range(duration): #loop through the days
        temp = []
        for fish in school:
            if fish == 0:
                temp.append(6)
                temp.append(8)
            else:
                temp.append(fish - 1)
        school = temp
        #print(school)
    #print(school)
    part1End = time.time()
    print("Number of fish after ", duration, " days is ", len(school))
    print("Part 1 runtime: ", part1Start - part1End, "\n")

    #print(init)
    #print(init.count(3))

    
    part2Start = time.time()
    print("Day 6 Part 2: ")
    duration = 256 #much longer date... exponential growh requires new technique
    schoolBins = np.zeros(9) #each bin represents the number of each age that we have
    for i in range(len(schoolBins)):
        schoolBins[i] = init.count(i)
    print("Initial Bins: ", schoolBins)

    for day in range(duration):
        new = schoolBins[0]
        for i in range(len(schoolBins)-1):
            schoolBins[i] = schoolBins[i+1]
        schoolBins[6] = schoolBins[6] + new
        schoolBins[8] = new
        #print(schoolBins)
    
    part2End = time.time()
    print("Number of fish after ", duration, " days is ", sum(schoolBins))
    print("Part 2 runtime: ", part2Start - part2End, "\n")
    


