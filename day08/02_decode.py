"""

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

"""

known_lengths = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}

with open('input.txt', 'r') as f:
    sol = 0
    for line in f.read().splitlines():
        p, output = line.split(' | ')
        digits = [''.join(sorted(digit)) for digit in output.split(' ')]
        patterns = [''.join(sorted(pattern)) for pattern in p.split(' ')]

        solvmap = {}
        revmap = {}

        for pattern in patterns:

            if len(pattern) in known_lengths:
                n = known_lengths[len(pattern)]
                solvmap[pattern] = n
                revmap[n] = set(pattern)

        for pattern in patterns:
            patset = set(pattern)

            if len(pattern) == 6: # its a 0, 6 or 9
                if not patset >= revmap[1]: # 6 is the only 6-seg not superset of 1
                    solvmap[pattern] = 6
                elif patset >= revmap[4]: # 9 is superset of 4's segments
                    solvmap[pattern] = 9
                else:
                    solvmap[pattern] = 0
            elif len(pattern) == 5: # 2, 3, 5
                if patset >= revmap[1]:
                    solvmap[pattern] = 3
                elif (patset | revmap[4]) == revmap[8]: # ok, 2 is the only one of these that satisfies "segments | segments_of_4 == segments_of_8"
                    solvmap[pattern] = 2
                else:
                    solvmap[pattern] = 5
        
        ps = sum([solvmap[digit] * (10 ** (3-i)) for i, digit in enumerate(digits)])
        print(ps)

        sol += ps

    print(sol)