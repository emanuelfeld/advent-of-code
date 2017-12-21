import re

with open('input.txt', 'r') as infile:
    data = infile.readlines()
    maze = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            maze[(i, j)] = data[i][j].strip()


y = 0
for i in range(len(data[0])):
    if data[0][i] != " ":
        x = i
        break

vx, vy = 0, 1
letters = []
steps = 0

while True:
    steps += 1
    if re.match(r'[A-Z]', maze[(x, y)]):
        letters.append(maze[(x, y)])
    if maze[(x+vx, y+vy)]:
        x += vx
        y += vy
    elif maze[(x+vy, y+vx)]:
        x += vy
        y += vx
        vx, vy = vy, vx
    elif maze[(x-vy, y-vx)]:
        x -= vy
        y -= vx
        vx, vy = -vy, -vx
    else:
        break


print('part 1:', ''.join(letters))
print('part 2:', steps)
