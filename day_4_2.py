from parse import *

card_copies = list()

def run():
    cards = list()
    with open("day_4_input.txt") as cards_file:
        cards = cards_file.readlines()

    card_copies = [1 for x in range(0,len(cards))]

    card_counter = 0

    for card in cards:
        card_points = 0
        parsed_card = parse("Card {card_id:>d}: {winning_numbers} | {card_numbers}", card.strip())
        winning_numbers = parsed_card['winning_numbers'].split()
        card_numbers = parsed_card['card_numbers'].split()
        for card_number in card_numbers:
            if card_number in winning_numbers:
                card_points += 1
        
        this_card_copies = card_copies[card_counter]
        
        if card_points != 0:
            for c in range(card_counter + 1, card_counter + 1 + card_points):
                card_copies[c] += this_card_copies

        card_counter += 1

    total_cards = sum(card_copies)

    print(total_cards)


if __name__ == "__main__":
    run()