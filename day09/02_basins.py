import collections
import functools

with open('input.txt', 'r') as f:
    hm = [list(map(int, line)) for line in f.read().splitlines()]

    lowpoints = []

    risk = 0
    for row in range(100):
        for col in range(100):
            neighvals = [hm[row + i][col + j] for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)] if row+i in range(100) and col+j in range(100)]
            if hm[row][col] < min(neighvals):
                lowpoints.append((row, col))

    basins = []
    for row, col in lowpoints:
        todo = collections.deque([(row, col)])
        basin = []
        seen = set()

        while todo:
            (r, c) = todo.pop()
            if (r, c) in seen:
                continue  # on with the next
            
            seen.add((r, c))
            if hm[r][c] < 9:
                basin.append((r, c))
                todo.extend( [ (r+i, c+j) for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)] if r+i in range(100) and c+j in range(100)])
        
        basins.append(len(basin))
    
print(functools.reduce(lambda x, y: x* y, sorted(basins)[-3:]))