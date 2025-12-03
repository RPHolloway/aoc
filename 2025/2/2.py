INPUT = "input.txt"

class Range:
    def __init__(self, range:str) -> None:
        self.start, self.end = map(int, range.split("-"))

def read_input(filename):
    with open(filename, "r") as file:
        return file.read().strip()

def parse_input(input:str) -> list[Range]:
    return [Range(range) for range in input.split(",")]

def part1(ranges):
    result = 0

    for r in ranges:
        for x in range(r.start, r.end+1):
            l = len(str(x))
            if l % 2 == 0:
                half = l // 2
                first_half = str(x)[:half]
                second_half = str(x)[half:]
                if first_half == second_half:
                    result += x
    
    return result

def part2(ranges):
    result = 0

    for r in ranges:
        for x in range(r.start, r.end+1):
            l = len(str(x))
            found = False

            for y in range(2, 11):
                if y > l: break
                if found: break

                if l % y == 0:
                    slice = l // y
                    for i in range(0, l, slice):
                        a = str(x)[i:i+slice]
                        b = str(x)[i+slice:i+(2*slice)]
                        if a == b:
                            if i + (2*slice) >= l:
                                result += x
                                found = True
                                break
                        else:
                            break
    
    return result

def main():
    input = read_input(INPUT)
    ranges = parse_input(input)

    result = part1(ranges)
    print(f"Part 1: {result}")
    result = part2(ranges)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
