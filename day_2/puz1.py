input_file = open('input.txt', 'r')

max_colours = {
    "red": 12,
    "green": 13,
    "blue": 14
}

possible_games = []

count = 1

for line in input_file.readlines():
    game_possible = True

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

            this_max = max_colours[col]

            if(num > this_max):
                game_possible = False



    if(game_possible):
        possible_games.append(game)

    count += 1

# ['1', '2', '5']
total = 0
for game in possible_games:
    total += int(game)

print(f'Total = {total}')