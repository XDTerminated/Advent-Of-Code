# Advent of Code - Day 01 - Trebuchet |

# Taking in input
with open("day01_input.txt", "r") as input:
    input_lines = [line.strip() for line in input]

# Part 1 Solution
def part1(input_lines):
    sum = 0
    for string in input_lines: # Loops throug the list
        number = "" # Create a variable to store the digits in the string
        for j in string: # Loop through the string
            if j in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]: # Compare characters in string with this list to see if it is a number
                number = number + j

        number = int(number[0] + number[-1]) # Take the first and last digit of the number
        sum+=number # Add to final sum

    return sum

# Part 2 Solution
def part2(input_lines):

    for i in range(len(input_lines)): # Loop through all lines in input file
        input_lines[i] = input_lines[i].replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine") # Replaces all word numbers with integer representation

    
    return part1(input_lines) # Run Part 1 question

print(part1(input_lines))
print(part2(input_lines))