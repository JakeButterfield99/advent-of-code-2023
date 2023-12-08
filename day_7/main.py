hands = {}
hands_by_type = {}
hands_to_letters = {}

hands_order = [
    "high-card",
    "one-pair",
    "two-pair",
    "three-of-a-kind",
    "full-house",
    "four-of-a-kind",
    "five-of-a-kind",
]

card_to_letter = {
    "A": "a", 
    "K": "b", 
    "Q": "c", 
    "J": "d",
    "T": "e", 
    "9": "f", 
    "8": "g", 
    "7": "h", 
    "6": "i", 
    "5": "j", 
    "4": "k", 
    "3": "l",
    "2": "m",
}

def get_hand_split(cards):
    nums = {}
    keys = []
    for num in cards:
        try:
            nums[num] = nums[num] + 1
        except KeyError:
            nums[num] = 1
            keys.append(num)
    
    return nums, keys

def get_hand_type(cards):
    split, keys = get_hand_split(cards)
    
    # Five of a Kind
    if(len(split) == 1):
        return 'five-of-a-kind'
    
    # Four of a kind
    card_1 = split[keys[0]]
    card_2 = split[keys[1]]
    if(len(split) == 2):
        check1 = (card_1 == 4 and card_2 == 1)
        check2 = (card_2 == 4 and card_1 == 1)
        if(check1 or check2):
            return 'four-of-a-kind'

    # Full House
    if(len(split) == 2):
        check1 = (card_1 == 3 and card_2 == 2)
        check2 = (card_1 == 2 and card_2 == 3)
        if(check1 or check2):
            return 'full-house'

    # Three of a kind
    card_3 = split[keys[2]]
    if(len(split) == 3):
        for card in split:
            if(split[card] == 3):
                return 'three-of-a-kind'

    # Two Pair
    if(len(split) == 3):
        check1 = (card_1 == 2 and card_2 == 2)
        check2 = (card_2 == 2 and card_3 == 2)
        check3 = (card_3 == 2 and card_1 == 2)
        if(check1 or check2 or check3):
            return 'two-pair'

    # One Pair
    if(len(split) == 4):
        return 'one-pair'

    # High Card
    return 'high-card'

def has_joker(hand_split):
    try:
        hand_split["J"]
        return True
    except KeyError:
        return False

def get_hand_type_p2(cards):
    split, keys = get_hand_split(cards)

    print("type2", split, keys)
    
    # Five of a Kind
    if(len(split) == 1):
        return 'five-of-a-kind'
    
    # Four of a kind
    card_1 = split[keys[0]]
    card_2 = split[keys[1]]
    if(len(split) == 2):
        if(has_joker(split)):
            return 'five-of-a-kind'

        check1 = (card_1 == 4 and card_2 == 1)
        check2 = (card_2 == 4 and card_1 == 1)
        if(check1 or check2):
            return 'four-of-a-kind'

    # Full House
    if(len(split) == 2):
        check1 = (card_1 == 3 and card_2 == 2)
        check2 = (card_1 == 2 and card_2 == 3)
        if(check1 or check2):
            return 'full-house'

    # Three of a kind
    card_3 = split[keys[2]]
    if(len(split) == 3):
        for card in split:
            if(split[card] == 3):
                if(has_joker(split)):
                    return 'four-of-a-kind'

                return 'three-of-a-kind'

    # Two Pair
    if(len(split) == 3):
        check1 = (card_1 == 2 and card_2 == 2)
        check2 = (card_2 == 2 and card_3 == 2)
        check3 = (card_3 == 2 and card_1 == 2)
        if(check1 or check2 or check3):
            if(has_joker(split) and split["J"] == 2):
                return 'four-of-a-kind'

            if(has_joker(split) and split["J"] == 1):
                return 'full-house'

            if(has_joker(split)):
                return 'three-of-a-kind'

            return 'two-pair'

    # One Pair
    card_4 = split[keys[3]]
    if(len(split) == 4):
        if(has_joker(split)):
            if(split["J"] == 1):
                mx = 0
                for card in split:
                    if(mx == 0 or split[card] > mx):
                        mx = split[card]

                if(mx == 2):
                    return 'three-of-a-kind'

                return 'two-pair'

            if(split["J"] == 2):
                return 'three-of-a-kind'

        return 'one-pair'

    # High Card
    if(has_joker(split)):
        return 'one-pair'

    return 'high-card'

# convert cards to letters to be sorted
def get_hand_letters(cards):
    letters = ""
    for card in cards:
        letters += card_to_letter[str(card)]
    return letters

def part_1(input_file):
    for line in input_file.readlines():
        split = line.split(" ")
        cards = split[0].strip()
        bid = int(split[1].strip())

        letters = get_hand_letters(cards)
        hand_type = get_hand_type(cards)

        hands[cards] = bid
        hands_to_letters[letters] = cards
        hands_by_type[hand_type].append(letters)

    # Sort each card in each type
    total = 0
    rank = 1
    for hand_type in hands_by_type:
        hands_by_type[hand_type].sort(reverse=True)

        for letters in hands_by_type[hand_type]:
            cards = hands_to_letters[letters]
            bid = hands[cards]

            total += (bid * rank)
            rank += 1

    print(f'Total = {total}')

def part_2(input_file):
    # swap sort table for new J
    card_to_letter["J"] = "n"

    for line in input_file.readlines():
        split = line.split(" ")
        cards = split[0].strip()
        bid = int(split[1].strip())

        letters = get_hand_letters(cards)
        hand_type = get_hand_type_p2(cards)

        hands[cards] = bid
        hands_to_letters[letters] = cards
        hands_by_type[hand_type].append(letters)

    # Sort each card in each type
    total = 0
    rank = 1
    for hand_type in hands_by_type:
        hands_by_type[hand_type].sort(reverse=True)

        for letters in hands_by_type[hand_type]:
            cards = hands_to_letters[letters]
            bid = hands[cards]

            if 'J' in cards:
                print(f'Card {cards} - {hand_type}')

            total += (bid * rank)
            rank += 1

    print(f'Total = {total}')

def main():
    input_file = open('input.txt', 'r')

    for hand_type in hands_order:
        hands_by_type[hand_type] = []

    #part_1(input_file)
    part_2(input_file)


if __name__ == '__main__':
    main()