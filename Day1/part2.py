with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

s = 50
r = 0
for l in lines:
    dir = l[0]
    amt = int(l[1:])

    step = -1 if dir == 'L' else 1

    for _ in range(amt):
        s = (s + step) % 100
        if s == 0:
            r += 1

print(r)
       