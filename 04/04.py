with open('input.txt', 'r') as infile:
    data = infile.readlines()
    data = [row.split() for row in data]


# part 1


def is_valid_1(row):
    return len(row) == len(set(row))


def part_1(data):
    return sum([is_valid_1(row) for row in data])


def test_1():
    assert is_valid_1('aa bb cc dd ee'.split()) == True
    assert is_valid_1('aa bb cc dd aa'.split()) == False
    assert is_valid_1('aa bb cc dd aaa'.split()) == True
    print('part 1 tests pass')


test_1()

print(part_1(data))


# part 2


def is_valid_2(row):
    sorted_set = set()
    for word in row:
        sorted_word = tuple(sorted(list(word)))
        sorted_set.add(sorted_word)
    return len(row) == len(sorted_set)


def part_2(data):
    return sum([is_valid_2(row) for row in data])


def test_2():
    assert is_valid_2('abcde fghij'.split()) == True
    assert is_valid_2('abcde xyz ecdab'.split()) == False
    assert is_valid_2('a ab abc abd abf abj'.split()) == True
    assert is_valid_2('iiii oiii ooii oooi oooo'.split()) == True
    assert is_valid_2('oiii ioii iioi iiio'.split()) == False
    print('part 2 tests pass')


test_2()

print(part_2(data))
