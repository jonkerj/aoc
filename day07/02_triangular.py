import numpy as np

with open('input.txt', 'r') as f:
    initial = np.array(list(map(int, f.read().strip().split(','))))

def cost(solution):
    solvector = np.repeat([solution], len(initial))
    distances = np.abs(solvector - initial)

    return sum((distances * (distances + 1)) / 2)

mean = np.ceil(np.mean(initial))
median = np.median(initial)

lowest = None
for solution in range(int(median), int(mean) + 1):
    fuel = cost(solution)

    if not lowest or fuel < lowest:
        lowest = fuel
        print(f'sol {solution} costs {fuel}')