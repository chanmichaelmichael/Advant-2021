import copy
import numpy as np
import time
import scipy as sp
from scipy.optimize import minimize_scalar

with open("7-inputs.txt") as f:
    print("Day 7 Part 1:")
    part1Start = time.time()
    def fuelCost(target, initPos):
        output = 0
        for p in initPos:
            output = output + abs(p - target)
        return output
        
    ### inputs = list(map(int, f.readlines()[0].split(",")))
    init = [int(i) for i in f.readlines()[0].split(",")] #list comprehension
    hpos = np.array(init)
    target = np.average(hpos).round(0)
    print("Target is: ", target)
    res = minimize_scalar(fuelCost, args = hpos)
    part1End = time.time()
    print("Best position is: ", int(res.x.round(0)))
    print("Fuel spent is: ", int(res.fun.round(0)))
    print("Part 1 runtime: ", part1Start - part1End, "\n")
    
    print("Day 7 Part 2:")
    part2Start = time.time()
    def fuelCost2(target, initPos):
        output = 0
        #diff = np.unique(abs(initPos-target)) #unique list of differences
        for p in initPos:
            diff = abs(p - target)
            output = output + diff*(diff+1)/2
        return output
    
    """
    res = minimize_scalar(fuelCost2, args = hpos)
    """
    
    minPos = max(hpos)
    minFuel = fuelCost2(minPos, hpos)
    print("Initial guess position: ", minPos)
    print("Initial guess position fuel: ", minFuel)
    for test in range(min(hpos), max(hpos)):
        tempFuel = fuelCost2(test, hpos)
        if tempFuel < minFuel:
            minFuel = tempFuel
            minPos = test
    print("Best position is: ", minPos)
    print("Fuel spent is: ", minFuel)
    
    part2End = time.time()
    
    #print("Best position is: ", res.x, " rounded to ", int(res.x.round(0)))
    #print("Fuel spent is: ", res.fun, " rounded to ", int(res.fun.round(0)))
    print("Part 2 runtime: ", part2Start - part2End, "\n")