import argparse
import pathlib

from aocd import get_data

# Define input data file name
infile = 'input.txt'


def main():
    args = parse_arguments()

    # If user provided command-line arguments
    if args.day and args.year:
        save_data_for_day(args.year, args.day, infile)
    else:
        save_data_to_AoC_directories(infile)


def parse_arguments():
    """Set up command-line argument parser."""

    parser = argparse.ArgumentParser()

    # Define optional command-line arguments
    parser.add_argument('-d', '--day', type=int, choices=range(1, 26))
    parser.add_argument('-y', '--year', type=int, choices=range(2015, 2050))

    # Parse command-line arguments
    return parser.parse_args()


def save_data_for_day(year, day, infile='input.txt'):
    """Save input for specific Advent of Code puzzle."""

    # There should be only one directory for specific year and day
    path = [p for p in pathlib.Path.cwd().glob(f'**/{year}/{day:02d}*')]

    try:
        # Write text data to file
        path[0].joinpath(infile).write_text(get_data(day=day, year=year))
        print(f"Data saved to {path[0].joinpath(infile)}")
    except IndexError:
        print(
            f"No such directory {pathlib.Path.cwd().joinpath(f'{year}', f'{day:02d}_... ')}."
        )


def save_data_to_AoC_directories(infile='input.txt'):
    """Save input for all AoC puzzles if directories exist."""

    try:
        # Find all AOC puzzles directories
        paths = [p for p in pathlib.Path.cwd().glob('**/[0-2][0-9]_*')]
        if not paths:
            raise FileNotFoundError
    except FileNotFoundError:
        print(f'No directory for Advent of Code days in {pathlib.Path.cwd()}.')

    # Save to infile files, eventually refresh them
    for path in paths:
        day = path.name[1:2] if path.name[0] == '0' else path.name[:2]
        year = path.parent.name
        path.joinpath(infile).write_text(
            get_data(day=int(day), year=int(year))
        )


if __name__ == '__main__':
    main()
