import sys
from collections import defaultdict

file = open(f'{sys.path[0]}/input.txt', 'r')
fish_timers = file.readline().strip()
all_fish = [int(timer) for timer in fish_timers.split(',')]    

new_fish = 0
spawn_days = defaultdict(int)
n = len(all_fish)

for day in range(80):
    for i in range(n):
        all_fish[i] -= 1
        if (all_fish[i] == -1):
            all_fish[i] = 6
            new_fish += 1
            spawn_days[day + 9] += 1
    if (day in spawn_days):
        new_fish += spawn_days[day]
        spawn_days[day + 7] += spawn_days[day]
        spawn_days[day + 9] += spawn_days[day]

print(n + new_fish)
