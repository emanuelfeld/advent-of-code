from collections import defaultdict


with open('input.txt', 'r') as infile:
    data = infile.readlines()


# with networkx


import networkx as nx


G = nx.Graph()


for row in data:
    row = row.strip()
    node, neighbors = row.split(' <-> ')
    G.add_edges_from((node, neighbor) for neighbor in neighbors.split(', '))


print('with networkx')
print('part 1:', len(nx.node_connected_component(G, '0')))
print('part 2:', nx.number_connected_components(G))


# without networkx


def make_graph():
    graph = defaultdict(set)
    for row in data:
        u, neighbors = row.split(' <-> ')
        neighbors = map(lambda x : x.strip(','), neighbors.split())
        for v in neighbors:
            graph[u].add(v)
            graph[v].add(u)
    return graph


def node_connected_component(graph, node):
    queue = [node]
    seen = set(queue)
    while queue:
        u = queue.pop()
        for v in graph[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return seen


def number_connected_components(graph, nodes):
    num = 0
    seen = set()
    for i in nodes:
        if i in seen:
            continue
        queue = [i]
        num += 1
        while queue:
            u = queue.pop()
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
    return num


graph = make_graph()

print('without networkx')
print('part 1:', len(node_connected_component(graph, '0')))
print('part 2:', number_connected_components(graph, map(str, range(2000))))
