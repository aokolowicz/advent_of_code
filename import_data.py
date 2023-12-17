import argparse
import pathlib

from aocd import get_data

# Set up argument parser
parser = argparse.ArgumentParser()

# Define optional command-line arguments
parser.add_argument('-d', '--day', type=int, choices=range(1, 26))
parser.add_argument('-y', '--year', type=int, choices=range(2015, 2050))

# Parse command-line arguments
args = parser.parse_args()

# If user provided command-line arguments
if args.day and args.year:
    # List all `input.txt` files for year and day
    path = [
        p
        for p in pathlib.Path.cwd().glob(
            f'**/{args.year}/{args.day:02d}*/input.txt'
        )
    ]

    # There should be only one file for specific year and day
    # Write text data to this file
    path[0].write_text(get_data(day=args.day, year=args.year))

# If no command-line arguments
else:
    # Refresh data in all files
    for path in pathlib.Path.cwd().glob(f'**/input.txt'):
        day = (
            path.parent.name[1:2]
            if path.parent.name[0] == '0'
            else path.parent.name[:2]
        )
        year = path.parent.parent.name
        path.write_text(get_data(day=int(day), year=int(year)))
