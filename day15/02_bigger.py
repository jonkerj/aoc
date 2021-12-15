import queue

def dijkstra(riskmap):
    width = len(riskmap[0])
    height = len(riskmap)

    q = queue.PriorityQueue()
    q.put((0, (0, 0)))
    risks = {(0, 0): 0}

    while not q.empty():
        risk, (x,y) = q.get()
        for ax, ay in {(-1,0), (0,-1), (1,0),(0,1)}:
            nx, ny = x+ax, y+ay
            if nx not in range(width) or ny not in range(height):
                continue

            new_risk = risk + riskmap[ny][nx]

            if nx == width-1 and ny == height-1:
                return new_risk
            
            if (nx, ny) in risks and risks[nx, ny] <= new_risk:
                continue

            risks[nx,ny] = new_risk
            q.put((new_risk, (nx, ny)))

def clip(risk):
    return (risk - 1) % 9 + 1

with open('input.txt', 'r') as f:
    riskmap = [list(map(int,line)) for line in f.read().splitlines()]

    width = len(riskmap[0])
    height = len(riskmap)

    # make it 5 times "wider" first
    for n in range(1, 5):
        for y in range(height):
            riskmap[y] += [clip(r+n) for r in riskmap[y][:width]]
    # make it 5 times "higher"
    for n in range(1, 5):
        for y in range(height):
            riskmap.append([clip(r+n) for r in riskmap[y]])
    
    print(dijkstra(riskmap))