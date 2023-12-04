symbol_locations = dict()
connected_gear_locations = dict()

def check_adjacent_to_gear(x, y):
    for x_index in range(x-1, x+2):
        for y_index in range(y-1,y+2):
            if f"{x_index},{y_index}" in symbol_locations.keys():
                if symbol_locations[f"{x_index},{y_index}"] == "*":
                    return x_index, y_index
    return None


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
            adjacent_to_gear = False
            gear_char = 0
            gear_line = 0
            while character_counter < max_char and line[character_counter] in "0123456789":
                number += line[character_counter]
                if not adjacent_to_gear:
                    gear_location = check_adjacent_to_gear(character_counter, line_counter)
                    if gear_location is not None:
                        gear_char = gear_location[0]
                        gear_line = gear_location[1]
                        adjacent_to_gear = True
                character_counter += 1
            if number != "":
                if adjacent_to_gear:
                    # check if another number is adjacent to this gear
                    if f"{gear_char},{gear_line}" in connected_gear_locations.keys():
                        other_number = connected_gear_locations[f"{gear_char},{gear_line}"]
                        gear_ratio = int(number) * other_number
                        total += gear_ratio
                    else:
                        connected_gear_locations[f"{gear_char},{gear_line}"] = int(number)
            character_counter += 1
        line_counter += 1

    print(total)




if __name__ == "__main__":
    run()