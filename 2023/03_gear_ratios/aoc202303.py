import pathlib
import re
import sys

from aocd import submit


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]

def part1(schematic):
    """Solve part 1."""
    
    numbers = {}
    row = 0
    for line in schematic:
        for number in re.finditer(r'\d+', line):
            numbers[int(number.group(0))] = {'row': row, 'start': number.start(), 'end': number.end()}
        row += 1

    # TODO: Make it works :)
    for number in numbers:
        previous_line_idx = numbers[number]['row'] - 1
        if schematic[previous_line_idx]:
            previous_col_idx = numbers[number]['start'] - 1
            next_col_idx = numbers[number]['end'] + 1
            for indexes in range(previous_col_idx, next_col_idx):
                print(number, indexes)

    print(numbers)


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    # Check if user provided input file name
    if len(sys.argv) < 2:
        print('Provide input file name.')

    # Solve puzzle
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

        # Automated submission
        submit1 = input(f'Submit answer for part 1: {solutions[0]}? [y/N]: ')
        if submit1.lower() != 'y':
            print('Answer for part 1 not submitted.')
        else:
            submit(solutions[0], part='a', day=3, year=2023)

        submit2 = input(f'Submit answer for part 2: {solutions[1]}? [y/N]: ')
        if submit2.lower() != 'y':
            print('Answer for part 2 not submitted.')
        else:
            submit(solutions[1], part='b', day=3, year=2023)
