steps = 337


def part_1(steps, max_val):
    buff = [0]
    index = 0
    value = 0

    while value < max_val + 1:
        value += 1
        index = (index + steps) % value + 1
        buff.insert(index, value)

    return buff[buff.index(max_val) + 1]

print('part 1:', part_1(steps, 2017))


def part_2(steps, max_val):
    index = 0
    value = 0
    answer = None

    while value < max_val + 1:
        value += 1
        index = (index + steps) % value + 1
        if index == 1:
            answer = value

    return answer


print('part 2:', part_2(steps, 50000000))