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

def check_adjacent(grid, x, y, pattern="@"):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    adjacent_coords = [(1, -1), (1, 0), (1, 1),
                       (0, -1),         (0, 1), 
                       (-1,-1), (-1,0), (-1,1)]
    

    for dx, dy in adjacent_coords:
        x1, y1 = x + dx, y + dy
        if 0 <= y1 < rows and 0 <= x1 < cols:
            if grid[y1][x1] == pattern:
                count += 1

    return count

def part1(grid, remove=False):
    result = 0

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "@":
                adjacent = check_adjacent(grid, x, y)
                
                if adjacent < 4:
                    if remove:
                        grid[y][x] = "."

                    result += 1

    return result

def part2(grid):
    result = 0
    write_grid(grid)

    while True:
        removed = part1(grid, remove=True)
        result += removed
        write_grid(grid)
        if removed == 0:
            break

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
