import re

def run():
    lines = list()
    with open("day_1_input.txt") as input_file:
        lines = input_file.readlines()
    total = 0
    for line in lines:
        result = re.search(r"[a-z]*(\d)\S*(\d)[a-z]*", line.strip())
        if result is None:
            result = re.search(r"[a-z]*(\d)[a-z]*", line.strip())
            digit1 = result.group(1)
            digit2 = digit1
        else:
            digit1 = result.group(1)
            digit2 = result.group(2)
        number_string = digit1+digit2
        number = int(number_string)
        print(number)
        total += number
    print(total)

if __name__ == "__main__":
    run()