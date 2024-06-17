# Read an input file.
# Check that the number of red,green,blue cubes in each row doesn't exceed max number of each colour.
# disqualify the line if cubes exceeds max number in any colour.
# Sum the line number of all the remaining lines.

import re, sys

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# A function that takes:
# colour: a string from this set ("red", "green", "blue")
# line: a line to search for the colour in. e.g. Game 5: 2 red, 1 blue, 4 green; 6 blue, 2 green; 2 red, 5 green
# max_colour: The maximum n
# returns False if any number in the list exceeds the max_colour, else it returns true.
def check_colour_in_a_line(colour, line, max_colour) -> bool: 
    search_str = '(\d+)' + "(?:\s" + colour+ ")"
    # get a list of numbers for the given "colour" from line.
    colour_numbers = [int(n) for n in re.findall(search_str, line)]
    # Check numbers in the list don't exceed max_number
    if any(n > max_colour for n in colour_numbers):
        return False
    return True
    
def main() -> int:
    f = open("input.txt", "r")
    sum = 0
    for line in f:
        line_number = int(re.search("\d+",line).group())
        # Add line numer  to sum only if none of the values in it exceed the max values.
        if (check_colour_in_a_line("red",line,MAX_RED) and 
            check_colour_in_a_line("green",line,MAX_GREEN) and
            check_colour_in_a_line("blue",line,MAX_BLUE)):
                sum += line_number     
    print(sum)
    return 0

if __name__ == '__main__':
    sys.exit(main())