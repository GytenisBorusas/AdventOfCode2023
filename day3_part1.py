'''
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the 
water source, 
but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't 
expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix 
it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure 
out which one. If you can add up all the part numbers in the engine schematic, it should be easy to 
work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are 
lots of numbers and symbols you don't really understand, but apparently any number adjacent to a 
symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) 
do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 
114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part 
number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers 
in the engine schematic?
'''


import sys


def main():
    game_list = read_puzzle()
    games_separated = separate_games(game_list)
    min_ball_counts = min_color_balls(games_separated)
    # print(valid_games)
    count_sum = multiply_ball_counts(min_ball_counts)
    print(f"Total sum: {count_sum}")  # Print the list of first and last digits

def read_puzzle():
    words = []
    with open('day2_puzzle_input.txt', 'r') as file:
        for line in file:
            words.append(line)
    return words

def separate_games(game_list):
    game_dict = {}

    for game in game_list:
        # Splitting the string to separate the game number and the color counts
        parts = game.split(': ')
        game_number = parts[0].split(' ')[1]  # Extracting the game number
        color_counts = parts[1].split('; ')  # Splitting the color counts

        # Removing potential newline characters and adding to the dictionary
        game_dict[game_number] = [s.strip() for s in color_counts]

    # Printing the dictionary for troubleshooting
    # for key, value in game_dict.items():
    #     print(f"'{key}': {value}")
    
    return game_dict
    
def min_color_balls(games_separated):
    valid_games = {}
    for key, rounds in games_separated.items():
        red_count = green_count = blue_count = 0
            
        for round in rounds:       
            # Split the round into individual color counts
            color_counts = round.split(', ')

            for color_count in color_counts:
                parts = color_count.split()  # Split the string into count and color
                count = int(parts[0])  # Convert the count to an integer
                color = parts[1]  # Assign the color

                if color == 'red':
                    if red_count < count:
                        red_count = count
                elif color == 'green':
                    if green_count < count:
                        green_count = count
                elif color == 'blue':
                    if blue_count < count:
                        blue_count = count
                        
        valid_games[key] = [red_count, green_count, blue_count]  # Add only valid games to the dictionary

    return valid_games   

def multiply_ball_counts(ball_counts):

    ball_multiplication_sum = 0
    
    for key in ball_counts:
        game_balls_multiplied = int(ball_counts[key][0]) * int(ball_counts[key][1]) * int(ball_counts[key][2])
        ball_multiplication_sum = ball_multiplication_sum + int(game_balls_multiplied)
        print(game_balls_multiplied)
    
    print(ball_multiplication_sum)
    return ball_multiplication_sum

if __name__ == "__main__":
    main()
