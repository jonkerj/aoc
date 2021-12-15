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

with open('input.txt', 'r') as f:
    riskmap = [list(map(int,line)) for line in f.read().splitlines()]

    print(dijkstra(riskmap))


















