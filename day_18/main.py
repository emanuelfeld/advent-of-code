from collections import defaultdict

def get(n, val):
    try:
        return int(val)
    except ValueError:
        return regs[n][val]

def run(n):
    cmd, *vals = data[indices[n]]
    X = vals[0]
    if len(vals) == 2:
        Y = vals[1]

    if cmd == 'snd':
        queues[not n].append(get(n, X))
        sent[n] += 1
    elif cmd == 'set':
        regs[n][X] = get(n, Y)
    elif cmd == 'add':
        regs[n][X] += get(n, Y)
    elif cmd == 'mul':
        regs[n][X] *= get(n, Y)
    elif cmd == 'mod':
        regs[n][X] %= get(n, Y)
    elif cmd == 'jgz':
        if get(n, X) > 0:
            indices[n] += get(n, Y)
            return False
    elif cmd == 'rcv':
        if queues[n]:
            locked[n] = False
            regs[n][X] = queues[n].pop(0)
        else:
            if locked[not n]:
                return True
            else:
                locked[n] = True
                return False
    indices[n] += 1
    return False


if __name__ == "__main__":
    regs = [defaultdict(int), defaultdict(int)]
    regs[0]['p'] = 0
    regs[1]['p'] = 1

    queues = [[], []]
    locked = [False, False]
    indices = [0, 0]
    sent = [0, 0]

    with open('input.txt', 'r') as infile:
        data = infile.readlines()
        data = [row.strip().split() for row in data]

    deadlocked = False
    while not deadlocked:
        deadlocked = run(1) or run(0)

    print(sent[1])
