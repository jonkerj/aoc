import functools

#state = [3,4,3,1,2]
with open('input.txt', 'r') as f:
    state = list(map(int, f.read().strip().split(',')))

nums = [len([a for a in state if a == age]) for age in range(9)]
for n in range(256):
    born = nums[0]

    for age in range(8):
        nums[age] = nums[age+1]
    
    nums[8] = born
    nums[6] += born

print(sum(nums))