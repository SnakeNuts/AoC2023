from parse import *

def run():
    cards = list()
    total_points = 0
    with open("day_4_input.txt") as cards_file:
        cards = cards_file.readlines()
    for card in cards:
        card_points = 0
        parsed_card = parse("Card {card_id:>d}: {winning_numbers} | {card_numbers}", card.strip())
        winning_numbers = parsed_card['winning_numbers'].split()
        card_numbers = parsed_card['card_numbers'].split()
        for card_number in card_numbers:
            if card_number in winning_numbers:
                card_points = card_points * 2 if card_points > 0 else 1
        print(card_points)
        total_points += card_points
    print(total_points)



if __name__ == "__main__":
    run()