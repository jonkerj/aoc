import numpy as np

with open('input.txt', 'r') as f:
    initial = np.array(list(map(int, f.read().strip().split(','))))

median = np.median(initial)
pos = np.repeat([median], len(initial))
fuel = np.sum(np.abs(pos-initial))
print(fuel)