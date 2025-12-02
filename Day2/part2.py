with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

ranges = lines[0].split(',')

def is_repeated_pattern(s):
    return s in (s + s)[1:-1]



res = 0
for r in ranges:
    nums = r.split('-')
    left = int(nums[0])
    right = int(nums[1])
    for i in range(left, right + 1):
        if is_repeated_pattern(str(i)):
            res += i

print(res)
