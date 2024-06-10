from collections import deque

lines = [x.split() for x in open("example.txt")]

# [print(x) for x in lines]
items_counter = 1

for i in range(0, 20+1):
    for idx, monkey in enumerate(lines):
        if idx == items_counter:
            items = monkey[2:]
            items_counter += 7
            print(items)
