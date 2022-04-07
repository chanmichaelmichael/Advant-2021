import statistics as stat
import pandas as pd
from numpy import true_divide
import copy

def split_str(s):
    return [c for c in s]

print("Day 3 Part 1: ")
with open("3-inputs.txt") as f:
    inputs = [line.split("\n")[0] for line in f.readlines()]
    #print("first item is ",inputs[0])
    #gamma = []
    gamma = 0
    #epsilon = []
    epsilon = 0
    places = len(inputs[0]) #numer of digits in output

    #calculate the modes in each digit
    modes = [] 
    for i in range(places):
        modes.append(int(stat.mode([x[i] for x in inputs])))
    print("Modes are ", modes)

    for i in range(places):
        gamma += modes[i]* 2**(places-i-1)
        epsilon += abs(modes[i]-1)*2**(places-i-1)
    print("gamma rate is ", gamma)
    print("epsilon rate is ", epsilon)
    print("power consumption is ", gamma*epsilon, "\n\n")


    """
    inputs2 = []
    for lines in inputs:
        inputs2.append(split_str(lines))
    modes2 = [] 
    for i in range(places):
        modes2.append(int(stat.mode(inputs2[:][i])))
    print("Modes2 are ", modes2)
    """
 


    print("Day 3 Part 2: ")
    oxygen_generator = copy.deepcopy(inputs)
    c02_scrubber = copy.deepcopy(inputs)

    #look for oxygen generator rating
    
    #Oxygen generator
    print("Calculating oxygen generator rating...")
    i = 0    
    while len(oxygen_generator) > 1:
        temp = []
        change = 0
        #calculate the mode
        zeros = sum([x[i]=='0' for x in oxygen_generator])
        ones = sum([x[i]=='1' for x in oxygen_generator])
        #print("i is ", i)
        #print("zeros count: ", zeros)
        #print("ones count: ", ones)

        if ones >= zeros:
            comparison = 1
        else:
            comparison = 0
        #print("mode: ", comparison)

        #add only items that match the mode
        for line in oxygen_generator:
            if int(line[i]) == comparison:
                temp.append(line)
                change += 1
        oxygen_generator = temp.copy()
        #print("added ", change, " items")
        #print("\nsize of remaining list: ", len(oxygen_generator))
        #print(oxygen_generator)
        i += 1
    print("Oxygen generator rating is ", oxygen_generator)
    print("Oxygen generator rating in decimals is ", int(oxygen_generator[0],base = 2), "\n")


    
    print("Calculating C02 scrubber rating...")
    i = 0    
    while len(c02_scrubber) > 1:
        temp = []
        change = 0
        #calculate the mode
        zeros = sum([x[i]=='0' for x in c02_scrubber])
        ones = sum([x[i]=='1' for x in c02_scrubber])
        #print("i is ", i)
        #print("zeros count: ", zeros)
        #print("ones count: ", ones)

        if zeros <= ones:
            comparison = 0
        else:
            comparison = 1
        #print("mode: ", comparison)

        #add only items that match the mode
        for line in c02_scrubber:
            if int(line[i]) == comparison:
                temp.append(line)
                change += 1
        c02_scrubber = temp.copy()
        #print("added ", change, " items")
        #print("\nsize of remaining list: ", len(c02_scrubber))
        #print(c02_scrubber)
        i += 1
    print("C02 scrubber rating is ", c02_scrubber)
    print("C02 scrubber rating in decimals is ", int(c02_scrubber[0],base = 2), "\n")
    print("Life support rating: ", int(c02_scrubber[0],base = 2)*int(oxygen_generator[0],base = 2))
    

