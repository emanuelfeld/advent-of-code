with open('input.txt', 'r') as infile:
    data = infile.readlines()[0].strip().split(',')


def hex_displacement(x, y, z):
    return int((abs(x) + abs(y) + abs(z)) / 2)


def hex_position(moves):
    x,y,z = 0, 0, 0
    for mv in moves:
        if mv == 'n':
            x += 1
            y -= 1
        elif mv == 's':
            x -= 1
            y += 1
        elif mv == 'nw':
            x += 1
            z -= 1
        elif mv == 'ne':
            y -= 1
            z += 1
        elif mv == 'sw':
            y += 1
            z -= 1
        elif mv == 'se':
            x -= 1
            z += 1
        yield (x, y, z)


positions = [pos for pos in hex_position(data)]
displacements = [hex_displacement(*pos) for pos in positions]

d_final = displacements[-1]
d_max = max(displacements)

print('final displacement:', d_final)
print('maximum displacement:', d_max)
