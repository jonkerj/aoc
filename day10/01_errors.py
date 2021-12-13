import collections

pairs = {
    '(': ')',
    '<': '>',
    '{': '}',
    '[': ']',
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

with open('input.txt', 'r') as f:
    score = 0
    for line in f.read().splitlines():
        state = collections.deque()
        cor = False

        for char in line:
            if char in pairs:
                state.append(char)
            else:
                if len(state) == 0:
                    cor = True
                    break

                expected = pairs[state.pop()]

                if char != expected:
                    score += scores[char]
                    break

print(score)