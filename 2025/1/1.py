INPUT = "input.txt"

def read_input(filename):
    with open(filename, "r") as file:
        return file.read().strip().splitlines()

def parse_instruction(instruction:str) -> int:
    direction = instruction[0]
    value = int(instruction[1:])
    if direction == 'L':
        return -value
    else:
        return value

def part1(instructions:list[str]) -> int:
    location = 50
    password = 0

    for instruction in instructions:
        location = (location + parse_instruction(instruction)) % 100
        # print(f"Location: {location}")
        if location == 0:
            password += 1
    
    return password

def part2(instructions:list[str]) -> int:
    location = 50
    password = 0

    for instruction in instructions:
        value = parse_instruction(instruction)
        rotations = int(value/100)
        password += abs(rotations)

        value = value - (rotations * 100)

        if (location == 0):
            location += value
        else:
            location += value
            if (location > 99 or location <= 0):
                password += 1

        location = location % 100
    
    return password

def main():
    input = read_input(INPUT)
    result = part1(input)
    print(f"Part 1: {result}")
    result = part2(input)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
