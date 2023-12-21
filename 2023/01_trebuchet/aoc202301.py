import pathlib
import re
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

    # Define regex pattern to capture numeric and spelled digits
    pattern = '|'.join(
        list(spelled_digits.keys()) + [str(d) for d in spelled_digits.values()]
    )
    pattern = '(' + pattern + ')'

    two_digit_number_list = []

    # Find indexes of numeric and spelled digits, assign digits
    for line in calibration_lines:
        # Use finditer with positive lookahead (?=...) to find
        # all occurrences including overlapping matches
        digits = {
            match.start(): match.group(1)
            for match in re.finditer(f'(?=({pattern}))', line)
        }

        # Ensure digits were found in the line
        if digits:
            first_value = digits[min(digits)]
            first_digit = (
                int(first_value)
                if first_value.isdigit()
                else spelled_digits[first_value]
            )

            last_value = digits[max(digits)]
            last_digit = (
                int(last_value)
                if last_value.isdigit()
                else spelled_digits[last_value]
            )

        # Add number to the list
        two_digit_number_list.append(first_digit * 10 + last_digit)

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
        print("\n".join(str(solution) for solution in solutions))

        # Automated submission
        submit1 = input(f'Submit answer for part 1: {solutions[0]}? [y/N]: ')
        if submit1.lower() != 'y':
            print('Answer for part 1 not submitted.')
        else:
            submit(solutions[0], part='a', day=1, year=2023)

        submit2 = input(f'Submit answer for part 2: {solutions[1]}? [y/N]: ')
        if submit2.lower() != 'y':
            print('Answer for part 2 not submitted.')
        else:
            submit(solutions[1], part='b', day=1, year=2023)
