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


# this is easier to extend to part 2, but runs in O(n) instead of O(1)

def positions():
    x, y = 0, 0
    layer = 0

    yield (x, y)

    while True:
        layer += 1
        while x < layer:
            x += 1
            yield (x, y)
        while y < layer:
            y += 1
            yield (x, y)
        while x > -layer:
            x -= 1
            yield (x, y)
        while y > -layer:
            y -= 1
            yield (x, y)


def part_1(n):
    counter = 1
    for (x, y) in positions():
        if counter + 1 > n:
            return abs(x) + abs(y)
        counter += 1


def test_1_1():
    assert manhattan_distance(1) == 0
    assert manhattan_distance(12) == 3
    assert manhattan_distance(23) == 2
    assert manhattan_distance(1024) == 31
    print('part 1 - method 1 tests pass')


def test_1_2():
    assert part_1(1) == 0
    assert part_1(12) == 3
    assert part_1(23) == 2
    assert part_1(1024) == 31
    print('part 1 - method 2 tests pass')


test_1_1()
print('part 1 method 1 - steps from 277678 to the access port:', manhattan_distance(277678))

test_1_2()
print('part 2 method 2 - steps from 277678 to the access port:', part_1(277678))


# part 2


def part_2(input_value):
    grid = {
        (0, 0): 1
    }

    for (x, y) in positions():
        value = sum([grid.get((i, j), 0) 
            for i in range(x - 1, x + 2) 
            for j in range(y - 1, y + 2)])
        if value > input_value:
            return value
        else:
            grid[(x, y)] = value


print('part 2:', part_2(277678))
