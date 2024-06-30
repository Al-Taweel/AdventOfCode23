# Read an input file.
# Find numbers that are adjacent to a symbol.
# Sum those numbers
import re, sys
# Check if a given number in the schematic is a part number by checking its surrounding
# if a number is adjacent to a symbol, return True, otherwise return False.
# n is a tuple with: (number_str, schematic y location, schematic x start,  schematic x end)
# number_str: A string representation of the number to check. (Not used in the function)
# schematic y location: The line number in the schematic where the number_str exists
# schematic x start: The column number in the schematic where the number_str starts
# schematic x end: : The column number in the schematic where the number_str ends

def is_part_number(n,schematic):
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
            if schematic[y][x] in "@$£#%^|&*()`!\"?/<>-+=[]{\}\\,~":
                return(True)
    return False

def main() -> int:
    f = open("input.txt", "r")
    part_numbers = []
    schematic_array = []
    line_number = 0
    sum = 0
    p = re.compile("\d+")
    for line in f:
        schematic_array.append(list(line))    # split into chars
        for num in p.finditer(line):  # Find all numbers and their locations
            part_numbers.append((num.group(),line_number,num.start(),num.end()))
        line_number += 1
    for num in part_numbers:
        if is_part_number(num, schematic_array):
            sum += int(num[0])
    print(sum)

    return 0

if __name__ == '__main__':
    sys.exit(main())