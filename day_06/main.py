with open('input.txt', 'r') as infile:
    data = infile.readlines()
    data = [int(num) for num in data[0].split()]


def redistribute(blocks):
  available = max(blocks)
  from_index = next(i for i in range(len(blocks)) if blocks[i] == available)
  to_index = from_index + 1
 
  while available > 0:
    to_index = to_index % len(blocks)
    blocks[to_index] += 1
    blocks[from_index] -= 1
    to_index += 1
    available -= 1
  return blocks


def main(blocks):
  steps = 0
  states = set()
  state_cycle = {}

  while tuple(blocks) not in states:
    state = tuple(blocks)
    states.add(state)
    state_cycle[state] = steps
    
    blocks = redistribute(blocks)
    steps += 1

  return steps, steps - state_cycle[tuple(blocks)]


def test():
    iterations, cycles = main([0, 2, 7, 0])
    assert iterations == 5
    assert cycles == 4
    assert redistribute([0, 2, 7, 0]) == [2, 4, 1, 2]
    assert redistribute([2, 4, 1, 2]) == [3, 1, 2, 3]
    print('tests pass')


test()

print(main(data))
