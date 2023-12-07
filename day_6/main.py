races = {}

def parse_line(line, key):
    global races

    split = line.split(":")[1].strip()
    split = split.split(" ")
    count = 0

    for num in split:
        if(not num.isdigit()):
            continue

        try:
            races[count][key] = int(num)
        except KeyError:
            races[count] = {}
            races[count][key] = int(num)

        count += 1

def process_race(race_id):
    race = races[race_id]
    race_time = race["time"]
    wins = 0

    for speed in range(race_time):
        dist = speed * (race_time - speed)
        if(dist > race["record"]):
            wins += 1

    print(f'Race {race_id+1}: {wins} possible wins')

    return wins


def part_1(input_file):
    lines = input_file.readlines()
    parse_line(lines[0], 'time')
    parse_line(lines[1], 'record')

    total = 0
    for race_id in races:
        wins = process_race(race_id)

        if(total == 0):
            total = wins
        else:
            total = total * wins

    print(f'Part 1 total: {total}')


def part_2(input_file):
    lines = input_file.readlines()
    parse_line(lines[0], 'time')
    parse_line(lines[1], 'record')

    time = ""
    record = ""

    for race_id in races:
        race = races[race_id]
        time += str(race["time"])
        record += str(race["record"])

    time = int(time)
    record = int(record)
    wins = 0

    for speed in range(time):
        if(speed % 1000000 == 0):
            print("speed", speed)

        dist = speed * (time - speed)
        if(dist > record):
            wins += 1

    print('wins', wins)

def main():
    input_file = open('input.txt', 'r')

    #part_1(input_file)
    part_2(input_file)


if __name__ == '__main__':
    main()