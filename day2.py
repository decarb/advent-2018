from collections import Counter
import numpy as np

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
