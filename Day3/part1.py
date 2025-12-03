with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

nums = lines 
def find_largest(n):
    # n is a string
    res = -10000
    for i in range(len(n) - 1):
        l = n[i]
        rest = set(n[i + 1:])
        rest = list(map(int, rest))
        # pr/int(rest)
        res = max(res, int(l + str(max(rest))))
    return res

res = 0
for n in nums:
    res += (find_largest(n))

print(res)
