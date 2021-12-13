
with open('input.txt', 'r') as f:
    p = None
    i = 0
    for line in f:
        m = int(line.rstrip())

        if p is not None and m > p:
            i += 1

        p = m
    
    print(i)
