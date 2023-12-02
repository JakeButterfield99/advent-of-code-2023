input_file = open('input.txt', 'r')

max_colours = {
    "red": 12,
    "green": 13,
    "blue": 14
}

game_powers = []

for line in input_file.readlines():
    current_max = {
        "red": 0,
        "blue": 0,
        "green": 0
    }

    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    split = line.split(':')[0] # Game 1
    game = split.split(' ')[1] # 1

    game_sets = line.split(':')[1].strip() # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

    for g_set in game_sets.split(';'):
        g_set = g_set.strip() # 3 blue, 4 red
        
        for res in g_set.split(','):
            res = res.strip() # 3 blue
            res = res.split(' ') # [0]: 3, [1]: blue

            num = int(res[0])
            col = res[1]
            
            if(current_max[col] < num):
                current_max[col] = num

    power = current_max['red'] * current_max['blue'] * current_max['green']
    game_powers.append(power)
    print(f'Game {game}: {power}')

total = 0

for power in game_powers:
    total += int(power)

print(f'Total = {total}')