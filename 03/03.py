import math


# part 1


def ceil_to_odd_square(n):
    "Returns the nearest odd perfect square larger than n."
    out = math.floor(math.sqrt(n - 1))
    if out % 2 == 0:
        return int((out + 1) ** 2)
    else:
        return int((out + 2) ** 2)


def manhattan_distance(n):
    if n == 1:
        return 0
    else:
        sq_hi = ceil_to_odd_square(n)
        sq_lo = int((math.sqrt(sq_hi) - 2) ** 2)
        layer = int((math.sqrt(sq_hi) - 1) / 2)
        offset = (n - sq_lo) % int(math.sqrt(sq_hi) - 1)
        return (abs(offset - layer) + layer)


def test_1():
    assert manhattan_distance(1) == 0
    assert manhattan_distance(12) == 3
    assert manhattan_distance(23) == 2
    assert manhattan_distance(1024) == 31
    print('part 1 tests pass')


test_1()

print('steps from 277678 to the access port:', manhattan_distance(277678))


# part 2


def positions():
    x, y = 1, 0
    layer = 1

    while True:
        while y < layer:
            y += 1
            yield (x, y)
        while x > -layer:
            x -= 1
            yield (x, y)
        while y > -layer:
            y -= 1
            yield (x, y)
        while x < layer + 1:
            x += 1
            yield (x, y)
        layer += 1


def part_2(input_value):
    assignments = {
        (0, 0): 1, 
        (1, 0): 1
    }

    def getter(x, y):
        try:
            return assignments[(x, y)]
        except:
            return 0

    for (x, y) in positions():
        value = sum([getter(i, j) 
            for i in range(x - 1, x + 2) 
            for j in range(y - 1, y + 2)])
        if value > input_value:
            return value
        else:
            assignments[(x, y)] = value


print(part_2(277678))
