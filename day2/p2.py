# Read an input file.
# Check the number of red, green, blue cubes in each row.
# Find the max values for each colour in each line. 
# Calculate the "power" of the line by multipling the values for the 3 colours in each line.
# Sum the "power" values.

import re, sys

# A function that takes:
# colour: a string from this set ("red", "green", "blue")
# line: a line to search for the colour in. e.g. Game 5: 2 red, 1 blue, 4 green; 6 blue, 2 green; 2 red, 5 green

# returns the max value for the given "colour" number.
def max_colour_in_a_line(colour, line) -> int: 
    search_str = '(\d+)' + "(?:\s" + colour+ ")"
    # get a list of numbers for the given "colour" from line.
    colour_numbers = [int(n) for n in re.findall(search_str, line)]
    return max(colour_numbers)
    
def main() -> int:
    f = open("input.txt", "r")
    sum = 0
    for line in f:
        power = max_colour_in_a_line("red", line) * max_colour_in_a_line("green", line) * max_colour_in_a_line("blue", line)  
        sum += power     
    print(sum)
    return 0

if __name__ == '__main__':
    sys.exit(main())