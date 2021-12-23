import re
import sys
from math import prod
from collections import Counter

def intersects(a, b):
    return all(a[i] <= b[i + 1] and a[i + 1] >= b[i] for i in range(0, 5, 2))

def get_intersection_area(a, b):
    return tuple((min if i & 1 else max)(a[i], b[i]) for i in range(6))

def get_area(area):
    return prod(area[i + 1] - area[i] + 1 for i in range(0, 5, 2))

steps = [
    (line.split(' ')[0], tuple(map(int, re.findall(r'-?\d+', line))))
    for line in open(f'{sys.path[0]}/input.txt', 'r')
]

areas = Counter()

for step_type, new_area in steps:
    updated_areas = Counter()

    if (step_type == 'on'):
        updated_areas[new_area] += 1

    for area, value in areas.items():
        if (intersects(new_area, area)):
            intersection_area = get_intersection_area(new_area, area)
            updated_areas[intersection_area] -= value

    areas.update(updated_areas)

print(sum(get_area(area) * value for area, value in areas.items()))
