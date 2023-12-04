def startsWithNumberName(slice:str):
    if slice.startswith("one"):
        return '1'
    if slice.startswith("two"):
        return '2'
    if slice.startswith("three"):
        return '3'
    if slice.startswith("four"):
        return '4'
    if slice.startswith("five"):
        return '5'
    if slice.startswith("six"):
        return '6'
    if slice.startswith("seven"):
        return '7'
    if slice.startswith("eight"):
        return '8'
    if slice.startswith("nine"):
        return '9'
    return '0'
    


def run():
    lines = list()
    with open("day_1_input.txt") as input_file:
        lines = input_file.readlines()
    counter = 1
    total = 0
    for line in lines:
        line = line.strip()
        # forward...
        for counter in range(0,len(line)):
            if line[counter] in ['1','2','3','4','5','6','7','8','9']:
                digit1 = line[counter]
                print(f"digit 1 is {digit1}")
                break
            else:
                digit = startsWithNumberName(line[counter:])
                if digit != '0':
                    digit1 = digit
                    print(f"digit 1 is {digit1}")
                    break
        # backward...
        for counter in range(len(line)-1, -1, -1):
            if line[counter] in ['1','2','3','4','5','6','7','8','9']:
                digit2 = line[counter]
                print(f"digit 2 is {digit2}")
                break
            else:
                digit = startsWithNumberName(line[counter:])
                if digit != '0':
                    digit2 = digit
                    print(f"digit 2 is {digit2}")
                    break

        number = digit1 + digit2
        total += int(number)
        print(f"{number}")
    print(total)                

if __name__ == "__main__":
    run()