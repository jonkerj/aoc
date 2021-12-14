import collections

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    template = lines[0]
    rules = {pair: insert for (pair, insert) in map(lambda x: x.split(' -> '), lines[2:])}

    elements = collections.Counter(template)
    pairs = collections.Counter(template[i:i+2] for i in range(len(template)-1))

    for step in range(40):
        new = collections.Counter()
        for pair, count in pairs.items():
            if pair in rules:
                a, b = pair
                c = rules[pair]
                new[a+c] += count
                new[c+b] += count
                elements[c] += count
            else:
                new[pair] = count
        pairs = new

    print(max(elements.values()) - min(elements.values()))