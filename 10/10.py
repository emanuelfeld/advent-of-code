from functools import reduce


instructions = "199,0,255,136,174,254,227,16,51,85,1,2,22,17,7,192"


# part 1


def knot_hash(lengths, numbers):
    pos = 0
    skip = 0

    for length in lengths:
        to_flip = [(pos + i) % len(numbers) for i in range(length)]
        temp = list(numbers)
        for i in range(length):
            numbers[to_flip[i]] = temp[to_flip[-(i+1)]]
        pos += (length + skip)
        skip += 1

    return numbers


lengths = [int(i) for i in instructions.split(',')]
numbers = list(range(256))

knot_hashed = knot_hash(lengths, numbers)
print('part 1:', knot_hashed[0] * knot_hashed[1])


# part 2


def sparse_hash(inpt):
    result = []
    for i in range(0, 256, 16):
        sh = reduce(lambda x, y: x ^ y, inpt[i:i+16])
        result.append(sh)
    return result


def dense_hash(inpt):
    result = []
    for sh in inpt:
        dh = hex(sh)[2:].zfill(2)
        result.append(dh)
    return ''.join(result)


lengths = [ord(char) for char in instructions] + [17, 31, 73, 47, 23]
lengths = lengths * 64
numbers = list(range(256))

knot_hashed = knot_hash(lengths, numbers)
sparse_hashed = sparse_hash(knot_hashed)
dense_hashed = dense_hash(sparse_hashed)

print('part 2:', dense_hashed)
