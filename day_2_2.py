from parse import *

max_red = 12
max_green = 13
max_blue = 14

def run():
    with open("day_2_input.txt") as input:
        games = input.readlines()
        total_power = 0
        for game_string in games:
            game = parse("Game {game_id}: {sets}", game_string.strip())
            game_id = int(game['game_id'])
            game_R = 0
            game_G = 0
            game_B = 0
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
                if R > game_R:
                    game_R = R
                if G > game_G:
                    game_G = G
                if B > game_B:
                    game_B = B
            game_power = game_R * game_G * game_B 
            print(f"Game power = {game_power} ({game_R} * {game_G} * {game_B})")
            total_power += game_power
        print(total_power)
                    


if __name__ == "__main__":
    run()