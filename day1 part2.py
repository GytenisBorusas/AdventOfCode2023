'''
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
'''


import sys


def main():
    words = read_puzzle()
    converted_words = replace_words_to_digs(words)
    numbers = find_numbers(converted_words)
    sum = sum_of_all_numbers(numbers)
    print(sum)  # Print the list of first and last digits


def read_puzzle():
    words = []
    with open('day1_puzzle_input.txt', 'r') as file:
        for line in file:
            words.append(line.strip())
    return words

def replace_words_to_digs(words):
    number_dic = ["one": "1",
                  "two": "2",
                  "three": "3",
                  "four": "4",
                  "five": "5",
                  "six": "6",
                  "seven": "7",
                  "eight": "8",
                  "nine": "9"
                  ]


def find_numbers(converted_words):
    numbers = []
    for word in converted_words:
        number1 = find_first_digit(word)
        number2 = find_last_digit(word)
        if number1 is not None and number2 is not None:
            sum_of_two = str(number1) + str(number2)
            numbers.append(int(sum_of_two))
    return numbers

def find_first_digit(word):
    for char in word:
        if char.isdigit():
            return char
    return None        
            
                
def find_last_digit(word):
    for char in reversed(word):
        if char.isdigit():
            return char
    return None

def sum_of_all_numbers(numbers):
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers = sum_of_numbers + number
    return sum_of_numbers
    





if __name__ == "__main__":
    main()
