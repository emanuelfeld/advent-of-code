with open('input.txt', 'r') as infile:
    data = infile.readlines()


firewall = [tuple(map(int, row.split(': '))) for row in data]


# part 1

# period of a scanner is 2 * (depth - 1), so caught if
# layer is an integer multiple of the period (i.e. the
# times when it is back at the top of its range)


def part_1(firewall):
    sev = 0
    for layer, depth in firewall:
        if layer % (2 * depth - 2) == 0:
            sev += layer * depth
    return sev


def test_1():
    test_firewall = [(0, 3), (1, 2), (4, 4), (6, 4)]
    assert part_1(test_firewall) == 24
    print('part 1 tests pass')


test_1()

print('part 1:', part_1(firewall))


# part 2

# just offset the layer by the delay time
# increment delay until find a layer where
# not collisions occur


def part_2(firewall):
    delay = 0
    while True:
        for layer, depth in firewall:
            if (delay + layer) % (2 * depth - 2) == 0:
                break
        else:
            return delay
        delay += 1


def test_2():
    test_firewall = [(0, 3), (1, 2), (4, 4), (6, 4)]
    assert part_2(test_firewall) == 10
    print('part 2 tests pass')


test_2()

print('part 2:', part_2(firewall))
