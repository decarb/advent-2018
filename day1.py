import numpy as np
from itertools import cycle

vals = np.loadtxt('day1.txt')
start = 0

for val in vals: start += val

print(start)

seen = set()
new_val = 0
pool = cycle(vals)

for val in pool:
    new_val += val

    if new_val in seen:
        print(new_val)
        break
    else: seen.add(new_val)
