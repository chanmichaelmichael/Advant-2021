#https://adventofcode.com/2021/day/1

import numpy as np

with open("1-depths.txt") as f:
    depths2 = [int(line) for line in f.readlines()]
    #print(len(depths2))
    #print(depths2[0])
    #print(depths2[1])
    result = [there > here for here, there in zip(depths2,depths2[1:])]
    print("Part A answer is: ",sum(result))


with open("1-depths.txt") as f:
    depths = [int(line) for line in f.readlines()]
    sums = [a + b + c for a, b, c in zip(depths,depths[1:], depths[2:])]
    result = [there > here for here, there in zip(sums,sums[1:])]
    print("Part B answer is: ",sum(result))
    #result = [there > here for here, there in zip(depths2,depths2[1:])]
