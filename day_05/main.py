with open('input.txt', 'r') as infile:
    data = [int(row) for row in infile.readlines()]

# part 1

def part_1(data):
  index = 0
  steps = 0
  while True:
    try:
      move = data[index]
      data[index] += 1
      index += move
      steps += 1
    except IndexError:
      return steps


def test_1():
    assert part_1([0, 3, 0, 1, -3]) == 5
    print('part 1 tests pass')


test_1()

print(part_1(list(data)))


# part 2


def part_2(data):
  index = 0
  steps = 0
  while True:
    try:
      move = data[index]
      data[index] = data[index] - (move > 2) + (move < 3)
      index += move
      steps += 1
    except IndexError:
      return steps


def test_2():
    assert part_2([0, 3, 0, 1, -3]) == 10
    print('part 2 tests pass')


test_2()

print(part_2(list(data)))
