def gen(start, factor, check=None):
    x = start
    while True:
        x = (x * factor) % 2147483647
        if check is None or x % check == 0:
            yield x & 0xFFFF


a_gen_1 = gen(512, 16807)
b_gen_1 = gen(191, 48271)

n_1 = 40000000
cnt_1 = 0

for _ in range(n_1):
    a = next(a_gen_1)
    b = next(b_gen_1)
    cnt_1 += (a == b)

print('part 1:', cnt_1)


a_gen_2 = gen(512, 16807, 4)
b_gen_2 = gen(191, 48271, 8)

n_2 = 5000000
cnt_2 = 0

for _ in range(n_2):
    a = next(a_gen_2)
    b = next(b_gen_2)
    cnt_2 += (a == b)

print('part 2:', cnt_2)

