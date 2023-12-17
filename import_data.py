import argparse
import pathlib

from aocd import get_data


# Define input data file name
infile = 'input.txt'

# Set up argument parser
parser = argparse.ArgumentParser()

# Define optional command-line arguments
parser.add_argument('-d', '--day', type=int, choices=range(1, 26))
parser.add_argument('-y', '--year', type=int, choices=range(2015, 2050))

# Parse command-line arguments
args = parser.parse_args()

# If user provided command-line arguments
if args.day and args.year:
    # There should be only one directory for specific year and day
    path = [
        p for p in pathlib.Path.cwd().glob(f'**/{args.year}/{args.day:02d}*')
    ]

    try:
        # Write text data to file
        path[0].joinpath(infile).write_text(
            get_data(day=args.day, year=args.year)
        )
        print(f"Data saved to {path[0].joinpath(infile)}")
    except IndexError:
        print(
            f"No such directory {pathlib.Path.cwd().joinpath(f'{args.year}', f'{args.day:02d}_... ')}."
        )

# If no command-line arguments
else:
    try:
        # Find all AOC days directories
        paths = [p for p in pathlib.Path.cwd().glob(f'**/[0-2][0-9]_*')]
        if not paths:
            raise FileNotFoundError
    except FileNotFoundError:
        print(f'No directory for Advent of Code days in {pathlib.Path.cwd()}.')

    # Save to `input.txt` files, eventually refresh them
    for path in paths:
        day = path.name[1:2] if path.name[0] == '0' else path.name[:2]
        year = path.parent.name
        path.joinpath(infile).write_text(
            get_data(day=int(day), year=int(year))
        )
