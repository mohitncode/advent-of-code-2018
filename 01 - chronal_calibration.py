from itertools import accumulate, cycle
import sys

filename = sys.argv[1]

# Part 1
frequencies = [int(r.strip()) for r in open(filename)]
print("Part 1 - %d" % sum(frequencies))

# Part 2
seen = set()
for f in accumulate(cycle(frequencies)):
  if f in seen:
    print("Part 2 - %d" % f)
    break;
  else:
    seen.add(f)