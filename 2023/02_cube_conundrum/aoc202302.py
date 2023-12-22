import pathlib
import re
import sys

from aocd import submit


def parse(puzzle_input):
    """Parse input."""

    games = {}
    for line in puzzle_input.split('\n'):
        # Extract the game ID
        game_id = int(line[5:line.find(':')])

        # Get numbers and colors of cubes taken out of the bag
        cubes = re.split(r', |; ', line[line.find(':') + 2:])

        # Add data for a specific game ID
        games[game_id] = cubes
    
    return games


def part1(data):
    """Solve part 1."""

    # Define limits
    limits = {'red': 12, 'green': 13, 'blue': 14}
    total = 0

    for game_id, cubes in data.items():
        # Temporary dictionary to store cubes info for game ID
        temp = {}
        for cube in cubes:
            # Split into individual cubes
            number, color = cube.split(' ')
            number = int(number)
            # Store the maximum number for each color in temp
            if number > temp.get(color, 0):
                temp[color] = number
            else:
                temp.setdefault(color, number)

        # Check each color against its limits
        for color in limits:
            # Avoid KeyError
            temp.setdefault(color, 0)
            # Omit the game ID if number of cubes exceeds its limits
            if temp[color] > limits[color]:
                break
        else:
            total += game_id

    return total


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
            submit(solutions[0], part='a', day=2, year=2023)

        submit2 = input(f'Submit answer for part 2: {solutions[1]}? [y/N]: ')
        if submit2.lower() != 'y':
            print('Answer for part 2 not submitted.')
        else:
            submit(solutions[1], part='b', day=2, year=2023)
