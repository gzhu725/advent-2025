with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

s = 50
r = 0
for l in lines:
    if l[0] == 'L':
        # something
        s -= int(l[1:])
        if s < 0:
            s = (100 + s) % 100
    else: 
        # R 
        s += int(l[1:])
        if s >= 100:
            s = (s - 100) % 100
    if s == 0:
        r += 1

print(r)
