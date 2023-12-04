from parse import *

max_red = 12
max_green = 13
max_blue = 14

def run():
    with open("day_2_input.txt") as input:
        games = input.readlines()
        total = 0
        for game_string in games:
            game = parse("Game {game_id}: {sets}", game_string.strip())
            game_id = int(game['game_id'])
            game_possible = True
            sets = game['sets'].strip()
            for set in sets.split(';'):
                R = 0
                G = 0
                B = 0
                cubes = set.split(',')
                for cube in cubes:
                    parsed_cube = parse("{count:d} {colour}", cube)
                    match parsed_cube['colour']:
                        case 'red':
                            R += parsed_cube['count']
                        case 'green':
                            G += parsed_cube['count']
                        case 'blue':
                            B += parsed_cube['count']
                if R > max_red or G > max_green or B > max_blue:
                    game_possible = False
            if game_possible:
                print(f"game {game_id} is possible.")
                total += game_id
        print(total)
                    


if __name__ == "__main__":
    run()