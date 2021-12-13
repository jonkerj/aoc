import collections

pairs = {
    '(': ')',
    '<': '>',
    '{': '}',
    '[': ']',
}

values = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

with open('input.txt', 'r') as f:
    scores = []
    for line in f.read().splitlines():
        state = collections.deque()
        corrupt = False

        for char in line:
            if char in pairs:
                state.append(char)
            else:
                if len(state) == 0:
                    corrupt = True
                    break

                expected = pairs[state.pop()]

                if char != expected:
                    corrupt = True
                    break
        
        if not corrupt and len(state) > 0:
            s = 0
            for c in [pairs[c] for c in reversed(state)]:
                s = (s*5) + values[c]
            scores.append(s)
    
    print(sorted(scores)[int((len(scores)-1)/2)])