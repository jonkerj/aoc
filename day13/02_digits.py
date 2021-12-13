dots = set()
folds = []

with open('input.txt', 'r') as f:
    for line in f.read().splitlines():
        if ',' in line:
            dots.add(tuple(map(int,line.split(','))))
        if line.startswith('fold along'):
            coord = int(line.rsplit('=', 1)[-1])
            if 'y=' in line:
                folds.append((True, coord))
            if 'x=' in line:
                folds.append((False, coord))
    
    for horiz, coord in folds:
        # discard 'fold line'
        # fold + n => fold -n
        # fold=7: 8 => 6
        # fold=7: 10 => 4
        # new_y = 2*fold - y
        if horiz:
            to_flip = set([dot for dot in dots if dot[1] > coord])
            for dot in to_flip:
                dots.remove(dot)
                dots.add((dot[0], 2*coord-dot[1]))
        else:
            to_flip = set([dot for dot in dots if dot[0] > coord])
            for dot in to_flip:
                dots.remove(dot)
                dots.add((2*coord-dot[0], dot[1]))
    
    # render time!
    width = max([dot[0] for dot in dots])+1
    height = max([dot[1] for dot in dots])+1
    bitmap = [['.']*width for _ in range(height)]
    for dot in dots:
        bitmap[dot[1]][dot[0]]='#'
    for line in bitmap:
        print(''.join(line))
