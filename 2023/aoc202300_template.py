import pathlib
import sys

from aocd import submit

# Fill day and year in 47 and 53 line


def parse(puzzle_input):
    """Parse input."""


def part1(data):
    """Solve part 1."""


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
            submit(solutions[0], part='a', day=, year=)

        submit2 = input(f'Submit answer for part 2: {solutions[1]}? [y/N]: ')
        if submit2.lower() != 'y':
            print('Answer for part 2 not submitted.')
        else:
            submit(solutions[1], part='b', day=, year=)
