# state = [3,4,3,1,2]
with open('input.txt', 'r') as f:
    state = list(map(int, f.read().strip().split(',')))

for n in range(80):
    born = []

    for i in range(len(state)):
        if state[i] > 0:
            state[i] -= 1
        else:
            state[i] = 6
            born.append(8)
    state += born
    
print(len(state)) 