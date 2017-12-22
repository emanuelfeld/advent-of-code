from collections import defaultdict

with open('input.txt', 'r') as infile:
    data = [line.strip() for line in infile.readlines()]
    grid = defaultdict(lambda:'.')
    for y in range(len(data)):
        for x in range(len(data[y])):
            grid[(x, y)] = data[y][x]


def part_1(bursts):
    infections = 0

    # starting position
    y = int((len(data) - 1) / 2)
    x = int((len(data[0]) - 1) / 2)

    # starting velocity
    vx, vy = 0, -1

    for _ in range(bursts):
        if grid[(x,y)] == '.':
            grid[(x,y)] = '#'
            infections += 1
            # turn left
            vx, vy = vy, -vx
        else:
            grid[(x,y)] = '.'
            # turn right
            vx, vy = -vy, vx
        x += vx
        y += vy

    return infections

print('part 1:', part_1(10000))


def part_2(bursts):
    infections = 0

    # starting position
    y = int((len(data) - 1) / 2)
    x = int((len(data[0]) - 1) / 2)

    # starting velocity
    vx, vy = 0, -1

    for _ in range(bursts):
        if grid[(x,y)] == '.':
            grid[(x,y)] = 'W'
            # turn left
            vx, vy = vy, -vx
        elif grid[(x,y)] == 'W':
            grid[(x,y)] = '#'
            infections += 1
        elif grid[(x,y)] == '#':
            grid[(x,y)] = 'F'
            # turn right
            vx, vy = -vy, vx
        elif grid[(x,y)] == 'F':
            grid[(x,y)] = '.'
            # reverse
            vx, vy = -vx, -vy
        x += vx
        y += vy

    return infections

print('part 2:', part_2(10000000))
