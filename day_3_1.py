from lib2to3.pygram import Symbols

symbol_locations = dict()

def check_adjacent_symbols(x, y):
    for x_index in range(x-1, x+2):
        for y_index in range(y-1,y+2):
            if f"{x_index},{y_index}" in symbol_locations.keys():
                return True
    return False


def run():
    lines = list()
    with open("day_3_input.txt") as gridFile:
        lines = gridFile.readlines()

    max_char = 0

    # first pass, note location of symbols
    line_counter = 0
    for line in lines:
        character_counter = 0
        for character in line.strip():
            if character not in "0123456789.":
                symbol_locations[f"{character_counter},{line_counter}"] = character
            character_counter += 1
            if character_counter > max_char:
                max_char = character_counter
        line_counter += 1
    
    print(symbol_locations)


    # now, let's go through the numbers
    line_counter = 0
    total = 0
    for line in lines:
        character_counter = 0
        while character_counter < max_char:
            number = ""
            is_adjacent = False
            while character_counter < max_char and line[character_counter] in "0123456789":
                number += line[character_counter]
                if not is_adjacent:
                    is_adjacent = check_adjacent_symbols(character_counter, line_counter)
                character_counter += 1
            if number != "":
                print(f"Found {number}, and adjacent is {is_adjacent}")
                if is_adjacent:
                    total += int(number)
            character_counter += 1
        line_counter += 1

    print(total)




if __name__ == "__main__":
    run()