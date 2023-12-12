'''
--- Day 2: Cube Conundrum ---
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. 
It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They 
don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the 
bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll 
do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated 
list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue 
cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the 
Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would 
have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
'''


import sys


def main():
    game_list = read_puzzle()
    games_separated = separate_games(game_list)
    valid_games = valid_game_or_not(games_separated)
    #print(valid_games)
    count_sum = add_valid_games(valid_games)
    
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
    
def valid_game_or_not(games_separated):
    red_cubes = 14
    green_cubes = 13
    blue_cubes = 14
    valid_games = {}
    
    for key, rounds in games_separated.items():
        game_is_valid = True  # Assume the game is valid initially

        # Iterate through each round in the game
        for round in rounds:
            red_count = green_count = blue_count = 0  # Reset counts for each round

            # Split the round into color-count pairs and count them
            color_counts = round.split(', ')
            for color_count in color_counts:
                count, color = color_coun
                t.split()
                count = int(count)
                if color == 'red':
                    red_count += count
                elif color == 'green':
                    green_count += count
                elif color == 'blue':
                    blue_count += count

            # Check if the round is valid
            if red_count > red_cubes or green_count > green_cubes or blue_count > blue_cubes:
                game_is_valid = False  # Mark the game as invalid
                break  # No need to check further rounds if one is invalid

        if game_is_valid:
            valid_games[key] = rounds  # Add only valid games to the dictionary

    return valid_games
    
# checks game validity
def add_valid_games(valid_games):

    valid_game_sum = 0
    
    for key in valid_games:
        print(key)
        
        valid_game_sum = valid_game_sum + int(key)
    
    for key, value in valid_games.items():
            print(f"'{key}': {value}")  
        
    return valid_game_sum

if __name__ == "__main__":
    main()
