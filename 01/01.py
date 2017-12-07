with open('input.txt', 'r') as infile:
    digits = infile.readlines()[0]


# part 1


def part_1(data):
    digits_1 = str(data)
    digits_1 = digits_1 + digits_1[0]

    out = 0
    for i in range(len(digits_1) - 1):
        out += (digits_1[i] == digits_1[i+1]) * int(digits_1[i])
    return out


def test_1():
    assert part_1(1122) == 3
    assert part_1(1111) == 4
    assert part_1(1234) == 0
    assert part_1(91212129) == 9
    print('part 1 tests pass')


test_1()

print(part_1(digits))


# part 2


def part_2(data):
    digits_2 = str(data)
    n_digits_2 = len(digits_2)

    out = 0
    for i in range(n_digits_2):
        j = int(i + n_digits_2/2) % n_digits_2
        out += (digits_2[i] == digits_2[j]) * int(digits_2[i])
    return out


def test_2():
    assert part_2(1212) == 6
    assert part_2(1221) == 0
    assert part_2(123425) == 4
    assert part_2(123123) == 12
    assert part_2(12131415) == 4
    print('part 2 tests pass')


test_2()

print(part_2(digits))
