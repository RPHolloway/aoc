INPUT = "input.txt"

def read_input(filename):
    with open(filename, "r") as file:
        return file.read().strip()

def parse_input(input:str) -> list[str]:
    return input.splitlines()

def part1(banks, num_batteries=2):
    result = 0

    for bank in banks:
        b_idx = 0
        j_idx = 0
        joltage = ["0"] * num_batteries

        batteries = list(bank)
        for batteries_remaining in range(num_batteries, 0, -1):
            l_idx = 0
            for i, battery in enumerate(batteries[b_idx:len(batteries) - batteries_remaining + 1]):
                if int(battery) > int(joltage[j_idx]):
                    joltage[j_idx] = battery
                    l_idx = i

            j_idx += 1
            b_idx += l_idx + 1

        result += int("".join(joltage)) 

    return result

def part2(banks):
    return part1(banks, num_batteries=12)

def main():
    input = read_input(INPUT)
    parsed_input = parse_input(input)

    result = part1(parsed_input)
    print(f"Part 1: {result}")
    result = part2(parsed_input)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
