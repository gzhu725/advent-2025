from collections import deque 

with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

d = dict()
for l in lines:
    key, value = l.split(':')
    value = value.split(' ')
    d[key] = value[1:]

queue = deque()
for v in d['you']:
    queue.append(v)

res = 0 
while queue:
     val = queue.popleft() 
     if val == 'out':
        res += 1
     else:
        for v in d[val]:
            queue.append(v)
print(res)