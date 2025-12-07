INPUT = "input.txt"

def read_input(filename):
    with open(filename, "r") as file:
        return file.read().strip()

def parse_input(input:str) -> list[list[str]]:
    return [list(row) for row in input.splitlines()]

def write_grid(grid, filename = "output.txt"):
    with open(filename, "w") as file:
        for row in grid:
            file.write("".join(row) + "\n")

def find_origin(row):
    for i, cell in enumerate(row):
        if cell == "S":
            return i

def part1(grid):
    result = 0
    beams = set()
    beams.add(find_origin(grid[0]))

    for i, row in enumerate(grid[1:]):
        new_beams = set()

        for beam in beams:
            if row[beam] == "^":
                new_beams.add(beam+1)
                new_beams.add(beam-1)
                result += 1

            else:
                new_beams.add(beam)
        
        beams = new_beams

        # Update grid for visualization
        for beam in beams:
            grid[i+1][beam] = "|"
        
        write_grid(grid)
        pass
    
    return result

def part2(grid):
    result = 0
    beams = {find_origin(grid[0]): 1}

    for i, row in enumerate(grid[1:]):
        new_beams = {}

        for x in beams:
            count = beams[x]

            if row[x] == "^":
                if x-1 in new_beams:
                    new_beams[x-1] += count
                else:
                    new_beams[x-1] = count

                if x+1 in new_beams:
                    new_beams[x+1] += count
                else:
                    new_beams[x+1] = count

            else:
                if x in new_beams:
                    new_beams[x] += count
                else:
                    new_beams[x] = count
        
        beams = new_beams

        # Update grid for visualization
        for x in beams:
            count = beams[x]
            grid[i+1][x] = str(count%10)
        
        write_grid(grid)
        pass
    
    result = sum(beams.values())
    return result

def main():
    input = read_input(INPUT)
    parsed_input = parse_input(input)
    result = part1(parsed_input)
    print(f"Part 1: {result}")

    input = read_input(INPUT)
    parsed_input = parse_input(input)
    result = part2(parsed_input)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
