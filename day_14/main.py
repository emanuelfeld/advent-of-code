import sys
sys.path.append('..')

from functools import reduce
from day_10.main import *


data = 'ljoxqyyw'


# part 1

def hash(data):
    lengths = [ord(char) for char in data] + [17, 31, 73, 47, 23]
    lengths = lengths * 64
    numbers = list(range(256))

    knot_hashed = knot_hash(lengths, numbers)
    sparse_hashed = sparse_hash(knot_hashed)
    dense_hashed = dense_hash(sparse_hashed)

    return dense_hashed


def part_1(data):
    grid = []
    used = 0

    for i in range(128):
        row = ''
        for char in hash(f'{data}-{i}'):
            row += str(bin(int(char, 16))[2:].zfill(4))
        row = list(map(int, list(row)))
        used += sum(row)
        grid.append(row)

    return grid, used


# part 2


def part_2(grid):
    def dfs(row, col):
        if ((row, col)) in visited:
            return
        elif grid[row][col] == 0:
            return
        visited.add((row, col))

        if row > 0:
            dfs(row - 1, col)
        if col > 0:
            dfs(row, col - 1)
        if row < 127:
            dfs(row + 1, col)
        if col < 127:
            dfs(row, col + 1)

    visited = set()
    groups = 0

    for row in range(128):
        for col in range(128):
            if (row, col) in visited:
                continue
            elif grid[row][col] == 0:
                continue
            groups += 1
            dfs(row, col)
    return groups


def test():
    test_data = 'flqrgnkx'
    grid, used = part_1(test_data)
    groups = part_2(grid)
    assert used == 8108
    assert groups == 1242
    print('tests passed')


test()

grid, used = part_1(data)
print('part 1:', used)
print('part 2:', part_2(grid))
