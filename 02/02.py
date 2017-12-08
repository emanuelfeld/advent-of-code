with open('input.txt', 'r') as infile:
    data = infile.readlines()
    data = [[int(digit) for digit in row.split()] for row in data]


# part 1


def part_1(data):
    return sum([max(row) - min(row) for row in data])


def test_1():
    assert part_1([
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8]]) == 18
    print('part 1 tests pass')


test_1()

print(part_1(data))


# part 2


def part_2(data):
    def row_value(row):
      row.sort()
      for i in range(len(row) - 1):
        for j in range(i + 1, len(row)):
          if row[j] % row[i] == 0:
            return int(row[j] / row[i])
    return sum([row_value(row) for row in data])


def test_2():
    assert part_2([
        [5, 9, 2, 8],
        [9, 4, 7, 3],
        [3, 8, 6, 5]]) == 9
    print('part 2 tests pass')

test_2()

print(part_2(data))
