import math 

class TrickShot:
    def __init__(self, tx0, tx1, ty0, ty1):
        self.tx0 = tx0
        self.tx1 = tx1
        self.ty0 = ty0
        self.ty1 = ty1
    
    def launch_probe(self, vx, vy):
        x = 0
        y = 0

        top = 0

        while x <= self.tx1 and y >= self.ty0:
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            vy -= 1

            top = max(y, top)
            if x >= self.tx0 and x <= self.tx1 and y >= self.ty0 and y <= self.ty1:
                return top

        return None
    
    def highest(self):
        h = -1
        for vx in range (0,self.tx1):
            for vy in range(self.ty0,-self.ty0):
                a = self.launch_probe(vx,vy)
                if a is not None and a > h:
                    h = a
        return h
    
    def velocities(self):
        r = set()
        for vx in range (self.tx1+1):
            for vy in range(self.ty0-1,-self.ty0+1):
                if t.launch_probe(vx,vy) is not None:
                    r.add((vx,vy))
        return r


t = TrickShot(253,280, -73, -46)
print(t.highest())
print(len(t.velocities()))
# x(s)  = -1/2 s^2 + 1/2 vs
# y(s)  = -1/2 s^2 + 1/2 vs
# y'(s) = -s + 1/2 v
# y'(s) = 0 => v=2s