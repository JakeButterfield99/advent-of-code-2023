input_file = open("input.txt", "r")
total = 0
count = 1

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for line in input_file.readlines():
    running = ""
    first = ""
    second = ""

    txt = line.strip()
    for char in txt:
        # Check if char is digit
        if(char.isdigit()):
            if(first == ""):
                first = char
            else:
                second = char
            
            # If digit, reset running string
            running = ""
        else:
            running = running + char

        for num, val in numbers.items():
            if num in running:
                if(first == ""):
                    first = str(val)
                else:
                    second = str(val)

                running = char
                break   

    if(second == ""):
        second = first

    l = first + second
    line_total = int(l)

    print(f'Line {count} = {line_total}')
    total = total + line_total
    count += 1

print(f'TOTAL = {total}')