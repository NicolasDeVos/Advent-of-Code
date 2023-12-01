#!/usr/bin/env python3

test_input = r"""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

test_input_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

translation_map = {
    'one' : '1',
    'two' : '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero' : '0'}

def find_digit(input, is_reverse = False):
    for index in range(len(input)):
        char = input[index] if is_reverse is False else input[len(input)-index-1]
        if char.isdigit():
            return char
        # added for part two:
        sub_str = input[:index+1] if is_reverse is False else input[len(input)-index-1:]
        for key in translation_map.keys():
            if key in sub_str:
                return translation_map[key]
    return None

def get_calibration_value(input):
    values = []
    for line in input:
        first_number = find_digit(line)
        last_number = find_digit(line, True) 
        value = int( first_number + last_number)
        values.append(value)
    print(values)
    return sum(values)

# Read input from text
content = test_input.split('\n')
print("Test result is {}, expected result is {}".format(get_calibration_value(content), 142))
content = test_input_2.split('\n')
print("Test result is {}, expected result is {}".format(get_calibration_value(content), 281))

# Read input from file
with open('input.txt', 'r') as f:
    content = f.read().splitlines()  # each line is a string

print("Result is {}".format(get_calibration_value(content)))
