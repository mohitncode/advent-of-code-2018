import sys
from collections import Counter
from itertools import combinations

filename = sys.argv[1]
box_ids = [l.strip() for l in open(filename)]

# Part 1
two_count = three_count = 0
for s in box_ids:
  counter = Counter(s)
  if 2 in counter.values(): two_count += 1
  if 3 in counter.values(): three_count += 1
print("Part 1 - %d" % (three_count * two_count))

# Part 2
for b1, b2 in combinations(box_ids, 2):
  distance = sum(1 for c1, c2 in zip(b1, b2) if c1 != c2)
  if 1 == distance:
    common = [x for x in b1 if x in b2]
    print("Part 2 - {}".format(''.join(common)))
    break