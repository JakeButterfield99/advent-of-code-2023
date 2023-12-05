import threading
import math

seeds = []
seed_range = []
maps = {}

def get_inverse_map_val(key, val):
    map_val = val

    for src in maps[key]:
        data = maps[key][src]

        if(data["dest_start"] > val):
            continue

        max_rng = data["dest_start"] + data["range"]
        if(max_rng < val):
            continue

        y = val - data["dest_start"]
        y = y + src
        map_val = y

    return map_val

def get_map_val(key, val):
    map_val = val

    for src in maps[key]:
        data = maps[key][src]

        x = val - src
        res = data["dest_start"] + x
        max_rng = data["dest_start"] + data["range"]

        if((res >= data["dest_start"]) and (res <= max_rng)):
            map_val = res
    
    return map_val
        

def process_seeds():
    closest_location = 0
    for seed in seeds:
        soil = get_map_val("seed-to-soil", seed)
        fertilizer = get_map_val("soil-to-fertilizer", soil)
        water = get_map_val("fertilizer-to-water", fertilizer)
        light = get_map_val("water-to-light", water)
        temperature = get_map_val("light-to-temperature", light)
        humidity = get_map_val("temperature-to-humidity", temperature)
        location = get_map_val("humidity-to-location", humidity)

        print(f"Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}")

        if(closest_location == 0 or (location < closest_location)):
            closest_location = location

    print("Closest Location: ", closest_location)

def process_range(numbers, active_map):
    source_start = numbers[1]
    dest_start = numbers[0]
    range_len = numbers[2]

    maps[active_map][source_start] = {
        "dest_start": dest_start,
        "range": range_len
    }

def parse_numbers(numbers):
    parse = []
    numbers = numbers.strip()
    split = numbers.split(" ")

    for num in split:
        if(num.isdigit()):
            parse.append(int(num))

    return parse

def part_1():
    process_seeds()

# Check if seed is valid and fits in range
def check_seed(seed):
    for rng in seed_range:
        mn = rng[0]
        mx = mn + rng[1]

        if(seed > mx):
            continue

        if(seed < mn):
            continue

        return True

results = {}
rep = 0

def new_thread(base_num, tot_range, results, index, rep):
    valid = []

    for x in range(tot_range):
        check = x + base_num

        if(check % 1000000 == 0):
            rep += 1
            print(f'check = {check}, rep = {rep}')

        humidity = get_inverse_map_val("humidity-to-location", check)
        temperature = get_inverse_map_val("temperature-to-humidity", humidity)
        light = get_inverse_map_val("light-to-temperature", temperature)
        water = get_inverse_map_val("water-to-light", light)
        fertilizer = get_inverse_map_val("fertilizer-to-water", water)
        soil = get_inverse_map_val("soil-to-fertilizer", fertilizer)
        seed = get_inverse_map_val("seed-to-soil", soil)

        if(check_seed(seed)):
            print(f'GOT SEED idx={index}, seed={seed}, loc={check}')
            valid.append(check)
            break

    results[index] = valid

def part_2():
    global seed_range

    biggest_loc = 0
    for src in maps["humidity-to-location"]:
        data = maps["humidity-to-location"][src]
        loc = data["dest_start"] + data["range"]

        if(biggest_loc == 0 or (loc > biggest_loc)):
            biggest_loc = loc

    print("big loc", biggest_loc)

    # Get seed ranges
    seed_range = []
    current_range = []
    add = False
    for seed in seeds:
        if(add):
            current_range.append(seed)
            seed_range.append(current_range)
            add = False
        else:
            current_range = []
            current_range.append(seed)
            add = True

    valid_locations = []

    # got loc iterations (1073741824, 268435456, 134217728) and was too high, try lower split
    biggest_loc = 134217728

    by_four = math.ceil(biggest_loc / 4)

    t1 = threading.Thread(target=new_thread, args=(0, by_four, results, 1, rep))
    t2 = threading.Thread(target=new_thread, args=(by_four, (by_four * 2), results, 2, rep))
    t3 = threading.Thread(target=new_thread, args=((by_four * 2), (by_four * 3), results, 3, rep))
    t4 = threading.Thread(target=new_thread, args=((by_four * 3), biggest_loc, results, 4, rep))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    valid_locations.extend(results[1])
    valid_locations.extend(results[2])
    valid_locations.extend(results[3])
    valid_locations.extend(results[4])

    lowest_loc = 0
    for loc in valid_locations:
        if(lowest_loc == 0 or (loc < lowest_loc)):
            lowest_loc = loc

    print("LOWEST LOC =", lowest_loc)



def main():
    input_file = open('input.txt', 'r')

    global maps
    global seeds

    line_no = 1
    active_map = ''

    for line in input_file.readlines():
        if(line.strip() == ""):
            line_no += 1
            continue

        # Line 1 is slightly different
        if(line_no == 1):
            split = line.split(":")
            seeds = parse_numbers(split[1])
            line_no += 1
            continue

        # Check for header
        if ":" in line:
            title = line.split(" ")
            active_map = title[0]
            maps[active_map] = {}
            line_no += 1
            continue

        # Is number map (49 53 8)
        numbers = parse_numbers(line)
        process_range(numbers, active_map)

        line_no += 1

    #part_1()
    part_2()


if __name__ == '__main__':
    main()