from random import shuffle

ll = list(input())

target = int(input())
targets = set()
values_map = {}

for value in ll:
    if value in targets:
        p1 = value
        p2 = values_map[int(value)]
        print(f"{p1} + {p2} = {target}")
    else:
        targets.add(target - (value))
        values_map[target - (value)] = value
