# Read an input file.
# Take the 1st & last digit of each line and join them as a number
# Sum all the numbers.

f = open("input.txt", "r")
sum = 0
for line in f:
    digits = [n for n in line if n in "0123456789"]
    number = int(digits[0]+digits[-1])
    sum += number
print(sum)
