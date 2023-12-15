from aocd import get_data

with open('input.txt', 'w') as infile:
    infile.save(get_data(day=1, year=2023))