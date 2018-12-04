import sys
import re

fabric = [[[] for i in range(1000)] for j in range(1000)]
filename = sys.argv[1]

pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
results = [pattern.match(l.strip()) for l in open(filename)]
overlaps = {}
for match in results:
  claim_id = int(match.group(1))
  x, y = int(match.group(2)), int(match.group(3))
  h, w = int(match.group(4)), int(match.group(5))
  if claim_id not in overlaps: overlaps[claim_id] = set()
  for i in range(x, x + h):
    for j in range(y, y + w):
      claimants = fabric[i][j]
      claimants.append(claim_id)
      if len(claimants) > 1:
        for c in claimants:
          overlaps[c].add(claim_id)
          overlaps[claim_id].add(c)

# Part 1
overlapping_area = sum(sum(1 for x in row if len(x) > 1) for row in fabric)
print("Part 1 - %d" % overlapping_area)

# Part 2
for claim_id in overlaps:
  if (0 == len(overlaps[claim_id])):
    print("Part 2 - %d " % claim_id)
    break
