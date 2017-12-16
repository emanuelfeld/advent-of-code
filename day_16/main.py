with open('input.txt', 'r') as infile:
    data = infile.readlines()
    sequence = data[0].strip().split(',')


progs = list('abcdefghijklmnop')


def dance(progs):
    for s in sequence:
        move = s[0]
        if move == 's':
            index = int(s[1:])
            progs = progs[-index:] + progs[:-index]
        elif move == 'x':
            a, b = map(int, s[1:].split('/'))
            progs[a], progs[b] = progs[b], progs[a]
        else:
            a, b = s[1:].split('/')
            a_index = progs.index(a)
            b_index = progs.index(b)
            progs[a_index], progs[b_index] = b, a
    return progs


print('part 1:', ''.join(dance(progs)))

# find length of cycle before see same program
# order

cycle = 1
seen = set([''.join(progs)])
while True:
    progs = dance(progs)
    if ''.join(progs) in seen:
        break
    else:
        cycle += 1
        seen.add(''.join(progs))

print('cycle length:', cycle)


iterations = (1000000000 % cycle)

for _ in range(iterations):
    progs = dance(progs)

print('part 2:', ''.join(progs))
