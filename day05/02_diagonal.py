import re

def lines():
    with open('input.txt', 'r') as f:
        for line in f.read().splitlines():
            m = re.match('(\d+),(\d+) -> (\d+),(\d+)', line)
            if m:
                yield tuple(map(int, m.groups()))

m = []
for y in range(1000):
    m.append([0] * 1000)

for x1, y1, x2, y2 in lines():
    # determine direction
    if x1 > x2:
        xd = -1
    elif x1 < x2:
        xd = 1
    else:
        xd = 0
    
    if y1 > y2:
        yd = -1
    elif y1 < y2:
        yd = 1
    else:
        yd = 0
    
    l = max(max(y1, y2) - min(y1, y2), max(x1, x2)-min(x1, x2))
    print(f'line: {xd},{yd} {l}')

    # start point
    m[y1][x1] += 1
    for i in range(1, l+1):
        m[y1 + i*yd][x1 + i*xd] += 1

n = 0
for y in range(1000):
    n += len([p for p in m[y] if p >= 2])
print(n)