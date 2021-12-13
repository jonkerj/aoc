with open('input.txt', 'r') as f:
    hm = [list(map(int, line)) for line in f.read().splitlines()]

    risk = 0
    for row in range(100):
        for col in range(100):
            neighvals = [hm[row + i][col + j] for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)] if row+i in range(100) and col+j in range(100)]
            if hm[row][col] < min(neighvals):
                risk += hm[row][col] + 1
    
    print(risk)