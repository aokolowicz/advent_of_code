import pathlib
import sys

from aocd import submit


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]


def part1(calibration_lines):
    """Solve part 1."""

    two_digit_number_list = []

    for line in calibration_lines:
        digits = [int(char) for char in line if char.isdigit()]
        # Ensure digits were found in the line
        if digits:
            two_digit_number_list.append(digits[0] * 10 + digits[-1])

    return sum(two_digit_number_list)


def part2(calibration_lines):
    """Solve part 2."""

    # spelled_digits = {
    #     'one': 1,
    #     'two': 2,
    #     'three': 3,
    #     'four': 4,
    #     'five': 5,
    #     'six': 6,
    #     'seven': 7,
    #     'eight': 8,
    #     'nine': 9,
    # }

    # for line in calibration_lines:
    #     # spelled = [line.find(digit) for digit in spelled_digits.keys()]
    #     spelled = {line.find(s_digit):n_digit for (s_digit, n_digit) in zip(spelled_digits.keys(), spelled_digits.values())}
    #     numeric = [line.find(char) for char in line if char.isdigit()]
        
    #     if spelled[0] < numeric[0]:



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions), '\n')

        # Automated submission
        submission1 = input(f'Submit answer for part 1: {solutions[0]}? [y/N]: ')
        if submission1.lower() != 'y':
            print('Answer for part 1 not submitted.')
        else:
            submit(solutions[0], part='a', day=1, year=2023)

        submission2 = input(f'Submit answer for part 2: {solutions[1]}? [y/N]: ')
        if submission2.lower() != 'y':
            print('Answer for part 2 not submitted.')
        else:
            submit(solutions[1], part='b', day=1, year=2023)
