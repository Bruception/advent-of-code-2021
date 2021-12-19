import sys
from itertools import permutations
from collections import defaultdict, deque

def permute(point):
    n = len(point)
    return [
        tuple(permutation[j] * (-1 if i & (1 << j) else 1) for j in range(n))
        for permutation in permutations(point, n)
        for i in range(1 << n)
    ]

class Scanner:
    def __init__(self, data):
        self.beacons = defaultdict(list)
        self.position = (0, 0, 0)
        self.orientation = 0

        for beacon in data[1:]:
            point = tuple(map(int, beacon.split(',')))
            for i, permutation in enumerate(permute(point)):
                self.beacons[i].append(permutation)
        
    def get_beacons(self):
        return self.beacons[self.orientation]

def add_positions(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

scanners = [
    Scanner(scanner.strip().split('\n'))
    for scanner in open(f'{sys.path[0]}/input.txt', 'r').read().split('\n\n')
]

known = deque(scanners[:1])
unknown = set(scanners[1:])

beacon_positions = set(scanners[0].get_beacons())

while (unknown):
    current_scanner = known.popleft()
    new_known_scanners = set()

    for scanner in unknown:
        for orientation, beacons in scanner.beacons.items():
            possible_positions = defaultdict(int)
            for beacon in beacons:
                for beacon2 in current_scanner.get_beacons():
                    dx = -beacon[0] + beacon2[0]
                    dy = -beacon[1] + beacon2[1]
                    dz = -beacon[2] + beacon2[2]
                    possible_positions[(dx, dy, dz)] += 1
            
            for position, overlap in possible_positions.items():
                if (overlap == 12):
                    new_known_scanners.add(scanner)
                    known.append(scanner)

                    scanner.position = add_positions(current_scanner.position, position)
                    scanner.orientation = orientation

                    for beacon in beacons:
                        beacon_positions.add(add_positions(beacon, scanner.position))
    
    unknown.difference_update(new_known_scanners)

print(len(beacon_positions))
