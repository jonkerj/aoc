ops = [
    ('forward', lambda h, d, a: (h+a, d)),
    ('up', lambda h, d, a: (h, d-a)),
    ('down', lambda h, d, a: (h, d+a)),
]

with open('input.txt', 'r') as f:
    h = 0
    d = 0
    for line in f:
        op, arg = line.rstrip().split(None, 1)
        arg = int(arg)

        for o, f in ops:
            if o == op:
                h, d = f(h, d, arg)
    
    print(f'h={h} d={d} solution={h*d}')
        