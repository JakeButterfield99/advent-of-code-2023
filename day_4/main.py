scores = []

# Parse the numbers
def parse_numbers(number_str):
    split = number_str.split(" ")
    numbers = []

    for num in split:
        num = num.strip()
        if num.isdigit():
            numbers.append(num)

    return numbers

# Get numbers from line
def get_numbers(line):
    numbers = line.split(":")[1]
    numbers = numbers.split("|")
    
    winning = parse_numbers(numbers[0])
    mine = parse_numbers(numbers[1])
    
    return {
        "winning": winning,
        "mine": mine,
    }

# Get card number from line
def get_card_number(line):
    card = line.split(":")[0]
    card = card.split(" ")
    num = 0
    
    for entry in card:
        if(entry.isdigit()):
            num = int(entry)
            break

    return num

def part_1(input_file):
    total = 0
    for line in input_file.readlines():
        card = get_card_number(line)
        numbers = get_numbers(line)

        value = 0
        for num in numbers["mine"]:
            if num in numbers["winning"]:
                if(value == 0):
                    value = 1
                else:
                    value = (value * 2)

        print(f'Card {card} value: {value}')
        total += value

    print(f"Total: {total}")


def part_2(input_file):
    card_copies = {}
    card_count = 0

    for line in input_file.readlines():
        card_count += 1
        card = get_card_number(line)
        numbers = get_numbers(line)
        copies = 0

        try:
            copies = card_copies[card]
        except KeyError:
            pass

        # Get how many winning numbers this card has
        winning_numbers = 0
        for num in numbers["mine"]:
            if num in numbers["winning"]:
                winning_numbers += 1

        if(winning_numbers == 0):
            pass

        print(f'Card {card} copies: {copies}, wins: {winning_numbers}')

        # Process new copies for this card + any existing copies
        # copies + 1 for this card
        for copy_idx in range(copies + 1):
            for winning_card in range(winning_numbers):
                new_card = card + int(winning_card + 1)
                try:
                    card_copies[new_card] = card_copies[new_card] + 1
                except KeyError:
                    card_copies[new_card] = 1

    # Get totals of cards
    total = 0
    for copy in card_copies:
        total += card_copies[copy]

    # Add original cards
    total += card_count
    print("total:", total)
        

def main():
    input_file = open('input.txt', 'r')

    #part_1(input_file)
    part_2(input_file)


if __name__ == '__main__':
    main()