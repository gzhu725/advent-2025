with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

ranges = list()
food = list()

for l in lines:
    if '-' in l:
        left = l.split('-')[0]
        right = l.split('-')[1]

        ranges.append((int(left),int(right)))
    elif l == '':
        continue 
    else:
        food.append(int(l))




# merge intervals on leetcode

ranges.sort()
merged = list()
for start, end in ranges:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)

print(merged)

res = 0
for m in merged:
    res += (m[1]-m[0] + 1)

print(res)
