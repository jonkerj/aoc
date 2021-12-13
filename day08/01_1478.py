with open('input.txt', 'r') as f:
    count = 0
    for line in f.read().splitlines():
        patterns, output = line.split(' | ')
        digits = output.split(' ')
        for digit in digits:
            if len(digit) in [2,4,3,7]:
                count += 1 
    print(count)
