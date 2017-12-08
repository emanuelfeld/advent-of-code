import re

with open('input.txt', 'r') as infile:
    data = infile.readlines()


def main(data):
    values = {}
    hi = 0

    for row in data:
        dst_var, op, val, src_var, cmp, cmp_val = re.match(r'(\w+) (inc|dec) (-?\d+) if (\w+) (\S+) (-?\d+)', row.strip()).groups()
        op = '+' if op == 'inc' else '-'
        dst = values.get(dst_var, 0)
        src = values.get(src_var, 0)
        expression = f'values["{dst_var}"] = {dst} {op} {val} if {src} {cmp} {cmp_val} else {dst}'
        exec(expression)
        hi = max(hi, max(values.values()))

    return max(values.values()), hi


def test():
    with open('test_input.txt', 'r') as infile:
        test_data = infile.readlines()
    max_at_end, max_ever = main(test_data)
    assert max_at_end == 1
    assert max_ever == 10
    print('tests pass')


test()

max_at_end, max_ever = main(data)
print('max at end:', max_at_end)
print('max ever:', max_ever)
