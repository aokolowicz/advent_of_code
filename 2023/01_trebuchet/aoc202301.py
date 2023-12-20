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
    # Fails

    spelled_digits = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    two_digit_number_list = []

    for line in calibration_lines:
        # Find indexes of spelled and numeric digits
        # TODO: digits can be spelled multiple times
        spelled = {line.find(s):n for (s, n) in spelled_digits.items() if line.find(s) != -1}
        numeric = [line.find(char) for char in line if char.isdigit()]
        
        # If lists are not empty
        if spelled and numeric:
            # Determine first and last digit based on index in line
            first_digit = spelled[min(spelled)] if min(spelled) < numeric[0] else int(line[numeric[0]])
            last_digit = spelled[max(spelled)] if max(spelled) > numeric[-1] else int(line[numeric[-1]])
        # If numeric is empty
        elif spelled:
            first_digit = spelled[min(spelled)]
            last_digit = spelled[max(spelled)]
        # If spelled is impty
        elif numeric:
            first_digit = int(line[numeric[0]])
            last_digit = int(line[numeric[-1]])

        two_digit_number_list.append(first_digit * 10 + last_digit)
        print(line, first_digit * 10 + last_digit)

    return sum(two_digit_number_list)


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
