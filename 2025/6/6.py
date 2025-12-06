INPUT = "input.txt"

def read_input(filename):
    with open(filename, "r") as file:
        return file.read()

def rotate_cw(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]

def rotate_ccw(matrix):
    return [list(row)[::-1] for row in zip(*matrix[::-1])]

def parse_part1(input):
    input = [row.split() for row in input.splitlines()]
    input = rotate_cw(input)
    return input

def part1(input):
    result = 0

    for row in input:
        x = 0
        operator = row[0].strip()

        if operator == "*":
            x = 1
            for cell in row[1:]:
                x *= int(cell)
        elif operator == "+":
            x = 0
            for cell in row[1:]:
                x += int(cell)
        
        result += x

    return result

def parse_part2(input):
    input = input.splitlines()
    i = 0
    start = 0
    end = 0
    problems = []

    while i < len(input[0]):
        blank_column = True

        for row in input:
            if row[i] != ' ':
                blank_column = False
                break
        
        i += 1
        if blank_column:
            end = i-1
            problems.append([list(r[start:end]) for r in input])
            start = i

    for i, row in enumerate(problems):
        problems[i] = rotate_ccw(row)
        pass

    return problems

def part2(input):
    result = 0
    problems = []

    for row in input:
        operator = row[0][-1]
        problem = [operator]
        for x in row:
            problem.append(''.join(x[:-1]).strip())
        
        problems.append(problem)

    result = part1(problems)

    return result

def main():
    input = parse_part1(read_input(INPUT))
    result = part1(input)
    print(f"Part 1: {result}")

    input = parse_part2(read_input(INPUT))
    result = part2(input)
    print(f"Part 2: {result}")

if __name__ == "__main__":
    main()
