def down(horiz, depth, aim, arg):
    return (horiz, depth, aim+arg)

def up(horiz, depth, aim, arg):
    return (horiz, depth, aim-arg)

def forward(horiz, depth, aim, arg):
    return (horiz+arg, depth+aim*arg, aim)

ops = {
    'down': down,
    'up': up,
    'forward': forward
}

with open('input.txt', 'r') as f:
    h = 0
    d = 0
    a = 0

    for line in f:
        op, arg = line.rstrip().split(None, 1)
        arg = int(arg)

        fn = ops[op]
        h, d, a = fn(h, d, a, arg)

    print(f'h={h} d={d} a={a} solution={h*d}')
        