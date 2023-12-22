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


def part1(games):
    """Solve part 1."""

    # Define limits
    limits = {'red': 12, 'green': 13, 'blue': 14}
    total = 0

    for game_id, cubes in games.items():
        temp = get_max(cubes)

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


def part2(games):
    """Solve part 2."""

    total = 0

    for cubes in games.values():
        temp = get_max(cubes)
        power = 1
        
        # Calculate the power of a set of cubes
        for number in temp.values():
            power *= number

        total += power
    
    return total


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


def get_max(game):
    """Find the maximum values for cubes colors in game."""

    # Temporary dictionary to store cubes info for game ID
    cubes_info = {}
    for cube in game:
        # Split into individual cubes
        cube_number, cube_color = cube.split(' ')
        cube_number = int(cube_number)

        # Store the maximum cube_number for each cube_color in temp
        if cube_number > cubes_info.get(cube_color, 0):
            cubes_info[cube_color] = cube_number
        else:
            cubes_info.setdefault(cube_color, cube_number)
    
    return cubes_info


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
