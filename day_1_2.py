import re

def numberToDigit(number):
    digit = 0
    match number:
        case "one":
            digit = 1
        case "two":
            digit = 2
        case "three":
            digit = 3
        case "four":
            digit = 4
        case "five":
            digit = 5
        case "six":
            digit = 6
        case "seven":
            digit = 7
        case "eight":
            digit = 8
        case "nine":
            digit = 9
        case _:
            digit = 0
    if digit == 0:
        digit = int(number)
    return digit
        

def run():
    lines = list()
    with open("day_1_input.txt") as input_file:
        lines = input_file.readlines()
    count = 1
    total = 0
    for line in lines:
        result = re.search(r"\S*?(one|two|three|four|fine|six|seven|eight|nine|[0-9])\S*(one|two|three|four|fine|six|seven|eight|nine|[0-9])\S*", line.strip())
        
        if result is None:
            result = re.search(r"\S*?(one|two|three|four|fine|six|seven|eight|nine|[0-9])\S*", line.strip())
            if result is None:
                print("Still not found!")
            else:
                number1 = result.group(1)
                number2 = number1
        else:
            number1 = result.group(1)
            number2 = result.group(2)

        digit1 = numberToDigit(number1)
        digit2 = numberToDigit(number2)

        number = (digit1 * 10) + digit2
        print(f"{count} - {number}")
        count += 1
        total += number

    print(total)

if __name__ == "__main__":
    run()