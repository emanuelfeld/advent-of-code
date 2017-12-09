with open('input.txt', 'r') as infile:
    data = infile.readlines()[0].strip()


def stream_processing(data):
    total = 0
    level = 0
    garbage_total = 0

    garbage = False
    canceled = False

    for char in data:
        if canceled: canceled = False
        elif char == '!': canceled = True
        elif char == '<' and garbage: garbage_total += 1
        elif char == '<': garbage = True
        elif char == '>': garbage = False
        elif garbage: garbage_total += 1
        elif char == '{': level += 1; total += level
        elif char == '}': level -= 1
    return total, garbage_total


print(stream_processing(data))
