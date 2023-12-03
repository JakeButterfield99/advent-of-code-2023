engine_numbers = []
engine_symbols = {}

star_symbols = {}
current_stars = []

banned_symbols = ["."]

symbols = []

def is_valid_symbol(char):
    if(char.isalnum()):
        return False
    if(char.isspace()):
        return False
    if(char == '.'):
        return False

    if(not char in symbols):
        symbols.append(char)
    
    return True

def is_breakpoint(char):
    if(char == '.'):
        return True
    if(is_valid_symbol(char)):
        return True

    return False

# Loop and log symbol positions
def find_symbols(lines):
    y_pos = 0

    for line in lines:
        engine_symbols[y_pos] = {}
        star_symbols[y_pos] = {}

        x_pos = 0
        for char in line:
            if(is_valid_symbol(char)):
                engine_symbols[y_pos][x_pos] = char

                if(char == "*"):
                    star_symbols[y_pos][x_pos] = []

            x_pos += 1
        y_pos += 1


def get_symbol(y, x):
    global current_stars

    try:
        if(engine_symbols[y][x]):
            if(engine_symbols[y][x] == "*"):
                current_stars.append({ 'x': x, 'y': y })
            return True
    except KeyError:
        return False

    return False


# check around for symbols
def check_for_symbols(y, x):
    symbols = []
    
    # left
    left = get_symbol(y, x-1)
    if(left):
        symbols.append(left)

    # right
    right = get_symbol(y, x+1)
    if(right):
        symbols.append(right)

    # up
    up = get_symbol(y-1, x)
    if(up):
        symbols.append(up)

    # below
    below = get_symbol(y+1, x)
    if(below):
        symbols.append(below)

    # diagonal bottom left
    diag_bot_left = get_symbol(y+1, x-1)
    if(diag_bot_left):
        symbols.append(diag_bot_left)

    # diagonal bottom right
    diag_bot_right = get_symbol(y+1, x+1)
    if(diag_bot_right):
        symbols.append(diag_bot_right)

    # diagonal up left
    diag_up_left = get_symbol(y-1, x-1)
    if(diag_up_left):
        symbols.append(diag_up_left)

    # diagonal up right
    diag_up_right = get_symbol(y-1, x+1)
    if(diag_up_right):
        symbols.append(diag_up_right)

    return (len(symbols) > 0)


def save_number(number, is_valid):
    global engine_numbers
    global current_stars

    if(is_valid):
        engine_numbers.append(number)

        for stars in current_stars:

            if(not number in star_symbols[stars['y']][stars['x']]):
                star_symbols[stars['y']][stars['x']].append(number)

        #print(f'save num {number} stars: {current_stars}')
        current_stars = []


def get_sum(nums):
    total = 0
    for num in nums:
        total += int(num)
    return total


# Search each number checking for valid symbols
def get_numbers(lines):
    y_pos = 0
    number = ""
    number_valid = False

    for line in lines:
        x_pos = 0

        for char in line:
            if(char.isdigit()):
                number += char
                valid = check_for_symbols(y_pos, x_pos)

                if(valid and (not number_valid)):
                    number_valid = True

            if(is_breakpoint(char) and (number != "")):
                save_number(number, number_valid)
                number = ""
                number_valid = False

            x_pos += 1

        y_pos += 1


def main():
    input_file = open("input.txt", "r")
    lines = input_file.readlines()

    find_symbols(lines)
    get_numbers(lines)

    total = get_sum(engine_numbers)

    print(f'got total {total}')

    gear_total = 0
    for y_star in star_symbols:
        for x_star in star_symbols[y_star]:
            if(len(star_symbols[y_star][x_star]) == 2):
                star_tbl = star_symbols[y_star][x_star]
                multiply = (int(star_tbl[0]) * int(star_tbl[1]))
                gear_total += multiply

    print(f'got gear total {gear_total}')


if __name__ == '__main__':
    main()