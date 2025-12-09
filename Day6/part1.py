with open('input.txt') as reader:
  lines = [line.strip() for line in reader.readlines()]

items = list()
for l in lines:
    l = l.split(' ')
    filtered_list = [item for item in l if item != '']
    items.append(filtered_list)


res = 0
operations = items[-1]
cur_res = 0
for i in range(len(items[0])):
    # each index
    cur_operation = operations[i]
    if cur_operation == '*':
        cur_res = 1
    else:
        cur_res = 0
    for l in items:
        # going thru each list 
        if l == operations:
            continue
        if cur_operation == '+':
            cur_res += int(l[i])
        elif cur_operation == '*':
            cur_res *= int(l[i])
    res += cur_res

print(res)

    

