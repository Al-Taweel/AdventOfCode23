# Read an input file.
# Take the 1st & last digit of each line and join them as a number
# digits can be 0-9 or text digits zero-nine
# Sum all the numbers.

import re

f = open("input.txt", "r")
sum = 0
str2digit = {
     "0":"0",
     "zero":"0",
     "1":"1",
     "one":"1",
     "2":"2",
     "two":"2",
     "3":"3",
     "three":"3",
     "4":"4",
     "four":"4",
     "5":"5",
     "five":"5",
     "6":"6",
     "six":"6",
     "7":"7",
     "seven":"7",
     "8":"8",
     "eight":"8",
     "9":"9",
     "nine":"9"
}
for line in f:
     # My original answer was wrong because 're' didn't take into account overlapping expressions.
     # For example: "twone" was interpreted as "2ne" by "re".
     # With overlapping expressions this becomes "21"
     # The spec wasn't clear about this point. 
     digits = re.findall('(?=(0|1|2|3|4|5|6|7|8|9|zero|one|two|three|four|five|six|seven|eight|nine))', line)
     num = int(str2digit[(digits[0])]+str2digit[digits[-1]])
     sum += num
print(sum)
