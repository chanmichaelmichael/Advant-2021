print("Part 1: ")
with open("2-inputs.txt") as f:
    horiz = 0
    depth = 0

    for line in f:
        movement = line.split(" ")[0]
        change = int(line.split(" ")[1])

        if movement == "forward":
            horiz += change

        elif movement == "up":
            depth -= change

        elif movement == "down":
            depth += change

print("Horizontal coord: ", horiz)
print("Depth coord: ", depth)
print("Product: ", horiz*depth,"\n")

print("Part 2: ")
with open("2-inputs.txt") as f:
    horiz = 0
    depth = 0
    aim = 0 #for part 2

    for line in f:
        movement = line.split(" ")[0]
        change = int(line.split(" ")[1])

        if movement == "forward":
            horiz += change
            depth += aim * change

        elif movement == "up":
            aim -= change

        elif movement == "down":
            aim += change

print("Horizontal coord: ", horiz)
print("Depth coord: ", depth)
print("Product: ", horiz*depth)