import sys
from collections import defaultdict, deque

def permute(point):
    permutations = []
    used, n = set(), len(point)

    def permute(permutation):
        if (len(permutation) == n):
            return permutations.append(tuple(permutation))
        
        for j, value in enumerate(point):
            if (j not in used):
                used.add(j)
                permute(permutation + [value])
                permute(permutation + [-value])
                used.remove(j)

    permute([])       

    return permutations

class Scanner:
    def __init__(self, data):
        self.name = data[0].split()[2]
        self.beacons = defaultdict(list)
        self.position = (0, 0, 0)
        self.orientation = 0

        for beacon in data[1:]:
            point = tuple(map(int, beacon.split(',')))
            for i, permutation in enumerate(permute(point)):
                self.beacons[i].append(permutation)
        
    def get_beacons(self):
        return self.beacons[self.orientation]

scanners = [Scanner(scanner.strip().split('\n')) for scanner in open(f'{sys.path[0]}/input.txt', 'r').read().split('\n\n')]

known = deque([scanners[0]])
unknown = set(scanners[1:])

all_beacons = set(scanners[0].get_beacons())

def add_positions(a, b):
    return tuple(p + p1 for p, p1 in zip(a, b))

while (known):
    current_scanner = known.popleft()
    new_known_scanners = set()

    for scanner in unknown:
        for orientation, beacons in scanner.beacons.items():
            possible_positions = defaultdict(int)
            for beacon in beacons:
                for beacon2 in current_scanner.get_beacons():
                    sx = -beacon[0] + beacon2[0]
                    sy = -beacon[1] + beacon2[1]
                    sz = -beacon[2] + beacon2[2]
                    possible_positions[(sx, sy, sz)] += 1
            
            for position, overlap in possible_positions.items():
                if (overlap >= 12):
                    new_known_scanners.add(scanner)
                    known.append(scanner)

                    scanner.position = add_positions(current_scanner.position, position)
                    scanner.orientation = orientation

                    for beacon in beacons:
                        all_beacons.add(add_positions(beacon, scanner.position))
    
    unknown.difference_update(new_known_scanners)

print(len(all_beacons))
