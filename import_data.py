import argparse
import pathlib

from aocd import get_data

# Set up the argument parser
parser = argparse.ArgumentParser()

# Define optional command-line arguments
parser.add_argument('-d', '--day', type=int, choices=range(1, 26))
parser.add_argument('-y', '--year', type=int, choices=range(2015, 2050))

# Parse the command-line arguments
args = parser.parse_args()

print(args.day, args.year)

if args.day and args.year:
    day = f'{args.day}'
    if args.day < 10:
        day = f'0{day}'

    pathlib.Path.cwd().glob(f'**/{args.year}/{day}*/input.txt')

else:
    # TODO: when no CL arguments - refresh data in all files
    for path in pathlib.Path.cwd().glob(f'**/input.txt'):
        print(path)

