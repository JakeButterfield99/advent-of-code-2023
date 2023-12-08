instructions = {}
order = []

def part_1():
    active_key = "AAA"
    dir_idx = 0
    steps = 0

    while(active_key != "ZZZ"):
        instr = instructions[active_key]
        direction = order[dir_idx]
        active_key = instr[direction]

        if(dir_idx == (len(order)-1)):
            dir_idx = 0
        else:
            dir_idx = dir_idx + 1

        steps += 1

    print("Got Steps:", steps)

def get_starting_nodes():
    nodes = []
    for key in instructions:
        letter = key[-1:]
        if letter == "A":
            nodes.append(key)
    return nodes

def nodes_valid(nodes):
    valid_nodes = []
    for node in nodes:
        letter = node[-1:]
        if letter == "Z":
            valid_nodes.append(node)
    
    return (len(valid_nodes) == len(nodes))

def part_2():
    active_nodes = get_starting_nodes()
    dir_idx = 0
    steps = 0

    while(not nodes_valid(active_nodes)):
        direction = order[dir_idx]
        next_nodes = []

        for node in active_nodes:
            instr = instructions[node]
            new_node = instr[direction]
            next_nodes.append(new_node)

        if(dir_idx == (len(order)-1)):
            dir_idx = 0
        else:
            dir_idx = dir_idx + 1

        steps += 1
        active_nodes = next_nodes


    print("Got Steps:", steps)

def main():
    input_file = open('input.txt', 'r')
    lines = input_file.readlines()

    line_count = 0
    for line in lines:
        line_count += 1

        # Get first value as instructions
        if line_count == 1:
            for char in line.strip(): # RL
                order.append(char)
            continue

        # If empty return
        if line.strip() == "":
            continue

        split = line.split("=")

        key = split[0].strip()
        instructions[key] = {}

        directions = split[1].split(",")
        left = directions[0].strip()[1:]
        right = directions[1].strip()[:-1]

        instructions[key]["L"] = left
        instructions[key]["R"] = right

    #part_1()
    part_2()


if __name__ == '__main__':
    main()