import copy
import numpy as np

print("Day 4 Part 1: ")
with open("4-inputs.txt") as f:
    inputs = [line.split("\n")[0] for line in f.readlines()]
    
    #isolate draws from board items 
    draws = copy.deepcopy(inputs[0])
    draws = draws.split(",")
    draws = [int(x) for x in draws]
    print("These are the draws: ")
    print(draws)
    print("\n")
    inputs = inputs[1:]

    #build out the boards as 2D array
    boards = []
    column_elements = []
    i = 1
    for item in inputs:
        if item != "":
            temp = item.split(" ")
            temp = [int(x) for x in temp if x != ""]
            column_elements.append(temp)
            if i == 5:
                boards.append(column_elements)
            i += 1
        else:
            column_elements = []
            i = 1
    
    boards = np.array(boards) #convert to array... is this helpful? 

    """
    for x in boards[:5]: 
        print (x, "\n")
    """

    

    winners = [] #to store our winners
    finalDraw = 0 #record last number drawn
    interaction = np.zeros(np.shape(boards)) #create size of interaction board
    maxScore = np.zeros(np.shape(boards)[0]) #a running record of all the boards' max scores
    for draw in enumerate(draws): #for each draw
        #print("Draw number ", draw[0], ". It is ", draw[1])
        for i in range(np.shape(boards)[0]): #for each board, calculate score
            maxTemp = 0
            match = boards[i] == draw[1]
            interaction[i] = interaction[i] + match
            #calculate maximum row score
            for x in range(5):
                temp = sum(interaction[i][x])
                maxTemp = max(maxTemp, temp)
            #calculate maximum column score
            for y in range(5):
                temp = sum(interaction[i][:,y])
                maxTemp = max(maxTemp, temp)
            maxScore[i] = maxTemp
            if maxTemp == 5:
                winners.append(i)
                finalDraw = draw[1]
        #print("\tmaximum score so far: ", max(maxScore))
        if(max(maxScore) == 5):
            break


    #print("max scores: ", maxScore)

    interaction2 = abs(interaction - 1)
    finalScores = []
    print("winner(s): board #", winners)
    print("winning board(s): ")
    for i in winners:
        print(boards[i])
        #print(interaction[i])
        #print(interaction2[i])
        temp = sum(sum(interaction2[i]*boards[i]))*finalDraw
        finalScores.append(temp)
        #print(np.dot(interaction2[i],np.transpose(boards[i])))
    print("final scores: ", finalScores, "\n")
    

    
    
    
    """
    print(boards[0])
    test = copy.deepcopy(boards[0])
    match = test == draws[0]
    print("match: \n", match)

    ## print(test2[:,0]) #this is how you select a column from 2d array
    
    print("interaction[0]: \n", interaction[0])
    print(interaction[0] + match)
    """



    print("Day 4 Part 2: ")
    lastWinDraw = 0
    orderedWinners = [] #to store ordered list of winners
    interaction = np.zeros(np.shape(boards)) #create size of interaction board
    maxScore = np.zeros(np.shape(boards)[0]) #a running record of all the boards' max scores
    gameEnd = False
    for draw in draws: #for each draw
        #print("Draw number ", draw[0], ". It is ", draw[1])
        for i in range(np.shape(boards)[0]): #for each board, calculate score
            maxTemp = 0
            match = boards[i] == draw
            interaction[i] = interaction[i] + match
            #calculate maximum row score
            for x in range(5):
                temp = sum(interaction[i][x])
                maxTemp = max(maxTemp, temp)
            #calculate maximum column score
            for y in range(5):
                temp = sum(interaction[i][:,y])
                maxTemp = max(maxTemp, temp)
            maxScore[i] = maxTemp
            if maxTemp == 5:
                if i not in orderedWinners:
                    orderedWinners.append(i)
                    if len(orderedWinners) == np.shape(boards)[0]: #if we have the last winner added
                        lastWinDraw = draw
                        gameEnd = True
                        break
            if gameEnd == True:
                break
        if gameEnd == True:
            break
        #print(interaction)
        #print("\n")

        #print("\tmaximum score so far: ", max(maxScore))

    interaction2 = abs(interaction - 1)
    
    print("Ordered winners: ", orderedWinners)
    print("Number of winners recorded: ", len(orderedWinners))
    lastID = orderedWinners[-1]
    print(lastID, " is the last board to win.")
    print(boards[lastID])
    print("Draw that makes board #", lastID, " win is ", lastWinDraw)
    print(interaction2[lastID])
    print("Final score for last board is ", sum(sum(interaction2[lastID]*boards[lastID]))*lastWinDraw)


