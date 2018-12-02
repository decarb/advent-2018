from collections import Counter
import numpy as np

# Part 1
data = [line.rstrip('\n') for line in open('day2.txt')]
two_count = 0
three_count = 0

for id in data:
    count_dict = Counter(id)
    two_done = False
    three_done = False

    for key in count_dict:
        count = count_dict[key]

        if count == 2 and not two_done:
            two_count += 1
            two_done = True
        if count == 3 and not three_done:
            three_count += 1
            three_done = True

print(two_count * three_count)


# Part 2
for i in range(len(data) - 1):
    id1 = data[i]

    for j in range(i + 1, len(data)):
        num_diff = 0
        pos = 0
        id2 = data[j]

        for index in range(len(id1)):
            if id1[index] != id2[index]:
                num_diff += 1
                pos = index

        if num_diff == 1: print(id1[:pos] + id1[pos + 1:])
