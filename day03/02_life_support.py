def filtor(haystack, mc):
    c = haystack

    for i in range(12):
        if len(c) == 1:
            break

        zeros = [code for code in c if code[i] == 0]
        ones = [code for code in c if code[i] == 1]

        if mc ^ (len(zeros) > len(ones)):
            c = ones
        else:
            c = zeros
    
    return sum([1 << n for n, bit in enumerate(reversed(c[0]), 0) if bit == 1])

with open('input.txt', 'r') as f:
    codes = f.read().splitlines()
    c = [[int(b) for b in code] for code in codes] # int-list-ify it

    oxygen = filtor(c, True)
    co2 = filtor(c, False)

    print(oxygen, co2)
    print(oxygen * co2)