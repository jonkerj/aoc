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
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            m[y][x1] += 1
    
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            m[y1][x] += 1

n = 0
for y in range(1000):
    n += len([p for p in m[y] if p >= 2])
print(n)