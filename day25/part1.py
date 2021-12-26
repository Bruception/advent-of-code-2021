import sys

sea_cucumbers = [list(line.strip()) for line in open(f'{sys.path[0]}/input.txt', 'r')]
n, m = len(sea_cucumbers), len(sea_cucumbers[0])

def step_right(sea_cucumbers):
    sea_cucumber_moved = False
    moved_sea_cucumbers = {}

    for i, row in enumerate(sea_cucumbers):
        for j, sea_cucumber in enumerate(row):
            if (sea_cucumber != '>'):
                continue
            
            dest_j = (j + 1) % m

            if (sea_cucumbers[i][dest_j] == '.'):
                moved_sea_cucumbers[(i, j)] = (i, dest_j)
                sea_cucumber_moved = True

    for (si, sj), (ei, ej) in moved_sea_cucumbers.items():
        sea_cucumbers[si][sj] = '.'
        sea_cucumbers[ei][ej] = '>'
    
    return sea_cucumber_moved

def step_down(sea_cucumbers):
    sea_cucumber_moved = False
    moved_sea_cucumbers = {}

    for i, row in enumerate(sea_cucumbers):
        for j, sea_cucumber in enumerate(row):
            if (sea_cucumber != 'v'):
                continue

            dest_i = (i + 1) % n

            if (sea_cucumbers[dest_i][j] == '.'):
                moved_sea_cucumbers[(i, j)] = (dest_i, j)
                sea_cucumber_moved = True

    for (si, sj), (ei, ej) in moved_sea_cucumbers.items():
        sea_cucumbers[si][sj] = '.'
        sea_cucumbers[ei][ej] = 'v'

    return sea_cucumber_moved

steps = 0
moved_right = moved_down = True

while (moved_right or moved_down):
    steps += 1
    moved_right = step_right(sea_cucumbers)
    moved_down = step_down(sea_cucumbers)

print(steps)
