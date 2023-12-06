# Advent of Code - Day 02 - Cube Conundrum |

with open("day02_input.txt", "r+") as input:
    input_lines = [line.strip() for line in input]

for i in range(len(input_lines)): # Loop through all lines in input file
        input_lines[i] = input_lines[i].replace(" red", "r").replace(" green", "g").replace(" blue", "b") # Replace with letters to make input easier to handle

# Extract Information
for i in range(len(input_lines)):
    input_lines[i] = input_lines[i].split(":")
    input_lines[i][1] = input_lines[i][1].split(";")
    input_lines[i][0] = input_lines[i][0][5::]
    for j in range(len(input_lines[i][1])):
        input_lines[i][1][j] = input_lines[i][1][j].split(",")

# Part 1
def solution(input_lines):
    sum = 0
    for i in range(len(input_lines)):
        n = True
        id = int(input_lines[i][0])
        for j in range(len(input_lines[i][1])):
            for k in range(len(input_lines[i][1][j])): # Looping through the list created above to get the individual numbers for each ball
                # Comparing the number to the max numnber of balls for that color and breaking out of the loop if it is greater than that.
                if input_lines[i][1][j][k][-1] == "r":
                    if int(input_lines[i][1][j][k][:-1]) > 12:
                        n = False
                        break

                if input_lines[i][1][j][k][-1] == "g":
                    if int(input_lines[i][1][j][k][:-1]) > 13:
                        n = False
                        break


                if input_lines[i][1][j][k][-1] == "b":
                    if int(input_lines[i][1][j][k][:-1]) > 14:
                        n = False
                        break

            if n == False:
                break

        if n == True:    
            sum+=id

    return sum

print(solution(input_lines))

# Part 2
def solution2(input_lines):
    sum = 0
    for i in range(len(input_lines)):
        smallestR = 0
        smallestG = 0
        smallestB = 0
        for j in range(len(input_lines[i][1])):
            for k in range(len(input_lines[i][1][j])):
                if input_lines[i][1][j][k][-1] == "r":
                    # Similar logic here except trying to find the maximum number of balls that are present for each game to make it possible
                    if int(input_lines[i][1][j][k][:-1]) > smallestR:
                        smallestR = int(input_lines[i][1][j][k][:-1])

                if input_lines[i][1][j][k][-1] == "g":
                    if int(input_lines[i][1][j][k][:-1]) > smallestG:
                        smallestG = int(input_lines[i][1][j][k][:-1])

                if input_lines[i][1][j][k][-1] == "b":
                    if int(input_lines[i][1][j][k][:-1]) > smallestB:
                        smallestB = int(input_lines[i][1][j][k][:-1])

        sum += (smallestB * smallestR * smallestG)
    return sum


print(solution2(input_lines))
