with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

ranges = lines[0].split(',')

res = 0
for r in ranges:
    nums = r.split('-')
    left = int(nums[0])
    right = int(nums[1])
    for i in range(left, right + 1):
        if len(str(i)) % 2 == 0:
            l = str(i)[0: len(str(i)) // 2]
            r = str(i)[len(str(i)) // 2 :]

            if l == r:
                res += i

print(res)
