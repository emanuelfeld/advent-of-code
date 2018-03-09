with open('input.txt', 'r') as infile:
    components = []
    data = infile.readlines()
    for line in data:
        component = list(map(lambda x: int(x.strip()), line.split('/')))
        components.append(component)

def run(curr_node, components, bridge=[]):
    for idx in range(len(components)):
        if curr_node in components[idx]:
            new_bridge = bridge + components[idx]
            new_components = components[:idx] + components[idx+1:]
            if components[idx][0] == curr_node:
                new_node = components[idx][1]
            else:
                new_node = components[idx][0]
            run(new_node, new_components, new_bridge)
    bridges.append(bridge)

bridges = []

run(0, components)

print('Part 1 weight:', max([sum(b) for b in bridges]))

max_len = 0
max_wt  = 0

for idx in range(len(bridges)):
    curr_len = len(bridges[idx])
    curr_wt = sum(bridges[idx])
    if curr_len > max_len:
        max_len = curr_len
        max_wt = curr_wt
    elif curr_len == max_len:
        if curr_wt > max_wt:
            max_wt = curr_wt

print('Part 2 weight:', max_wt)
