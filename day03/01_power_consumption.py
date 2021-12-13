def mc(bits):
    a = sum(bits) / len(bits)
    if a < 0.5:
        return 0
    return 1

def bin2num(bits):
    return sum([1 << n for n, bit in enumerate(reversed(bits), 0) if bit == 1])

with open('input.txt', 'r') as f:
    codes = f.read().splitlines()
    c = [[int(b) for b in code] for code in codes] # int-list-ify it
    r = list(zip(*c[::-1])) # rotate

    gam_bits = list(map(mc, r)) # 011101111100 ?
    eps_bits = [1-g for g in gam_bits]

    print(bin2num(gam_bits) * bin2num(eps_bits))

