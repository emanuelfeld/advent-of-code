import re
from collections import Counter 


class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None
        self.total_weight = None

    def add_children(self, nodes):
        self.children = nodes
        for node in nodes:
            node.parent = self

    def get_total_weight(self):
        self.total_weight = self.weight + sum([
            node.get_total_weight()
            for node in self.children])
        return self.total_weight


def parse_input(data):
    parent_set = set()
    child_set = set()
    nodes = {}

    for row in data:
        name = row.split(' (')[0]
        weight = int(re.search(r'[0-9]+', row)[0])
        nodes[name] = Node(name, weight)

    for row in data:
        if row.find('->') > -1:
            parent, children = re.split(r' \([0-9]+\) -> ', row)
            children = children.split(', ')
            nodes[parent].add_children([nodes[child] for child in children])
            parent_set.add(parent)
            child_set.update(children)

    root_name = list(parent_set.difference(child_set))[0]
    root = nodes[root_name]

    return root


def balance_tower(node):
    def get_child_weight_counts(node):
        count = Counter()
        for child in node.children:
            count[child.total_weight] += 1
        return count

    def get_weight_discrepancy(node):
        count = get_child_weight_counts(node)
        ordered_count = count.most_common()
        target_weight = ordered_count[0][0]
        wrong_weight = ordered_count[-1][0]
        return target_weight - wrong_weight

    def recur(node, discrepancy):
        child_weights = [child.total_weight for child in node.children]
        is_balanced = len(set(child_weights)) == 1

        if is_balanced:
            return node.weight + discrepancy
        else:
            weight_count = get_child_weight_counts(node)
            unbalanced_node = next((
                child for child in node.children 
                if weight_count[child.total_weight] == 1))
            return recur(unbalanced_node, discrepancy)

    discrepancy = get_weight_discrepancy(node)
    return recur(node, discrepancy)


def test():
    with open('test_input.txt', 'r') as infile:
        test_root = parse_input([line.strip() for line in infile.readlines()])
        test_root.get_total_weight()

    assert test_root.name == 'tknk'
    assert balance_tower(test_root) == 60
    print('tests pass')


test()

with open('input.txt', 'r') as infile:
    root = parse_input([line.strip() for line in infile.readlines()])
    root.get_total_weight()

print('root:', root.name)
print('new weight:', balance_tower(root))
