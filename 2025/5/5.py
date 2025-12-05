INPUT = "input.txt"

class Range:
    def __init__(self, range:str) -> None:
        self.start, self.end = map(int, range.split("-"))

def read_input(filename):
    with open(filename, "r") as file:
        return file.read().strip()

def parse_input(input:str):
    return input.split("\n\n")

def next_range(ranges):
    for r in ranges.splitlines():
        yield Range(r)

def next_ingredient(ingredients):
    for ingredient in ingredients.splitlines():
        yield int(ingredient)

def part1(input):
    result = 0

    for i in next_ingredient(input[1]):
        for r in next_range(input[0]):
            if i >= r.start and i <= r.end:
                result += 1
                break

    return result

def part2(input):
    result = 0
    ranges = sorted(next_range(input[0]), key=lambda r: r.start)
    r1 = Range("0-0")
    end = 0

    for r2 in ranges:
        overlap = 0
        if r2.start <= r1.end:
            overlap = r1.end - r2.start + 1

        if end >= r2.end:
            continue

        result += r2.end - r2.start + 1 - overlap
        r1 = r2
        end = r2.end

    return result

def main():
    input = read_input(INPUT)
    parsed_input = parse_input(input)

    result = part1(parsed_input)
    print(f"Part 1: {result}")
    result = part2(parsed_input)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
