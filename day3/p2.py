# Read an input file.
# Find any 2 numbers that are both adjacent to the same '*' symbol
# find the sum of the multiplications of all two numbers sharing a star.
import re, sys

# Check if a number in the schematic is adjacent to a star.
# n is is a tuple with: (number_str, schematic y location, schematic x start,  schematic x end)
# number_str: A string representation of the number to check. (Not used in the function)
# schematic y location: The line number in the schematic where the number_str exists
# schematic x start: The column number in the schematic where the number_str starts
# schematic x end: : The column number in the schematic where the number_str ends 
# Return value:
#       None if no adjacent star was found
#       [num,x,y] if a star is found. Where: 
#           num is the integer representation of number_str
#           x,y is the location of the '*' in the schematic
def is_number_adjacent_to_star(n, schematic):
    # set the limits of a rectangle envelope around the number
    horizontal_begin = n[2] - 1
    horizontal_end = n[3]
    vertical_begin = n[1]-1
    vertical_end = n[1] + 1
    
    # deal with edge cases.
    if horizontal_begin < 0:
        horizontal_begin = 0
    if vertical_begin < 0:
        vertical_begin = 0
    if horizontal_end >= len(schematic[n[1]]):
        horizontal_end = len(schematic[n[1]]) - 1
    if vertical_end >= len(schematic):
        vertical_end = len(schematic) - 1

    # Go through the envelope
    part_number_flag = False
    for y in range(vertical_begin, vertical_end+1):
        for x in range(horizontal_begin,horizontal_end+1):
            if schematic[y][x] == "*":
                return([int(n[0]),x,y])
    return None


def main() -> int:
    f = open("input.txt", "r")
    schematic_array = []
    numbers = []  # A list of numbers and their locations in the schematic
    starred_numbers_list = [] # A list of all numbers adjacent to a star and the star location.
    line_number = 0
    sum = 0
    p = re.compile("\d+")
    for line in f:
        schematic_array.append(list(line))    # split into chars
        for num in p.finditer(line):  # Find all numbers and their locations
            numbers.append((num.group(),line_number,num.start(),num.end()))
        line_number += 1
 
    # Find numbers adjacent to a '*'
    for num in numbers:
        starred_number = is_number_adjacent_to_star(num, schematic_array)
        if starred_number:
            starred_numbers_list.append(starred_number)

    # Sort the list of starred numbers based on the star's x,y locations
    starred_numbers_list.sort(key = lambda x:(x[1], x[2]))
    
    # Look for numbers that share the same '*' by comparing the x,y location of the '*' in the schematic 
    for n in range(len(starred_numbers_list)-1):
        if (starred_numbers_list[n][1]==starred_numbers_list[n+1][1] and
           starred_numbers_list[n][2]==starred_numbers_list[n+1][2]):
            # Calculate the part number value by multiplying the numbers that share the same star.git st
            sum += starred_numbers_list[n][0] * starred_numbers_list[n+1][0]
    print(sum)
    return 0

if __name__ == '__main__':
    sys.exit(main())