import collections
import itertools

with open('input.txt', 'r') as f:
    energy = [[int(c) for c in line] for line in f.read().splitlines()]
    flashes = 0

    for step in range(100):

        for y in range(10):
            for x in range(10):
                energy[y][x]+= 1
        
        flashable = [(y, x) for (y, x) in itertools.product(range(10), range(10)) if energy[y][x] > 9]
        seen = set(flashable)
        todo = collections.deque(flashable)

        while todo:
            (y, x) = todo.pop()

            for (i, j) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if y + i not in range(10) or x + j not in range(10):
                    continue
                energy[y+i][x+j] += 1
                if energy[y+i][x+j] > 9 and (y+i, x+j) not in seen:
                    seen.add((y+i, x+j))
                    todo.append((y+i, x+j))

        for y in range(10):
            for x in range(10):
                if energy[y][x] > 9:
                    energy[y][x] = 0
        
    print(flashes)