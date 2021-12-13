
with open('input.txt', 'r') as f:

    ringbuffer = []
    i = 0
    p = None
    for line in f:
        m = int(line.rstrip())

        ringbuffer.insert(0, m)
        ringbuffer = ringbuffer[:3]
        
        if len(ringbuffer) == 3:
            s = sum(ringbuffer)
            if p is not None and s > p:
                i += 1
            p = s
    
    print(i)
