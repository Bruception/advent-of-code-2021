import sys
import math
from functools import cache

burrow = [line for line in open(f'{sys.path[0]}/input.txt', 'r').read().split('\n')]
burrow.insert(3, '  #D#C#B#A#')
burrow.insert(4, '  #D#B#A#C#')

room_size = len(burrow) - 3 # 3 - To remove the first and last border + the hall.
room_doors = (2, 4, 6, 8)

target_room = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
movement_cost = {ch: 10 ** i for i, ch in enumerate('ABCD')}

hall_spots = (0, 1, 3, 5, 7, 9, 10)
target_room_state = tuple((ch,) * room_size for ch in 'ABCD')

def can_enter_room(pod, room):
    return all(ch == '.' or ch == pod for ch in room)

def path_is_clear(hall, start, end):
    direction = -1 if start > end else 1
    return all(hall[i] == '.' for i in range(start + direction, end + direction, direction))

def room_has_wrong_amphipod(room, room_index):
    return any(ch != '.' and target_room[ch] != room_index for ch in room)

@cache
def solve(hall, rooms):
    if (rooms == target_room_state):
        return 0

    best_cost = math.inf

    for i, amphipod in enumerate(hall): # Try moving amphipods from the hall into appropriate rooms
        if (amphipod == '.'):
            continue
        
        room_index = target_room[amphipod]
        room_door = room_doors[room_index]
        room = rooms[room_index]

        if (not (can_enter_room(amphipod, room) and path_is_clear(hall, i, room_door))):
            continue

        empty_spots = sum(ch == '.' for ch in room)

        new_room = ('.',) * (empty_spots - 1) + (amphipod,) * (room_size - empty_spots + 1)
        new_rooms = rooms[:room_index] + (new_room,) + rooms[room_index+1:]
        new_hall = hall[:i] + ('.',) + hall[i+1:]

        total_steps = empty_spots + abs(i - room_door)
        cost = total_steps * movement_cost[amphipod]
        total_cost = cost + solve(new_hall, new_rooms)

        best_cost = min(best_cost, total_cost)

    for i, room in enumerate(rooms): # Try moving amphipods from rooms into the hall
        if (not room_has_wrong_amphipod(room, i)):
            continue
        
        empty_spots = sum(ch == '.' for ch in room)
        amphipod = room[empty_spots]

        for hall_spot in hall_spots: # Try moving amphipod to all possible hall spots
            if (not path_is_clear(hall, room_doors[i], hall_spot)):
                continue
            
            new_room = ('.',) * (empty_spots + 1) + room[empty_spots+1:]
            new_rooms = rooms[:i] + (new_room,) + rooms[i+1:]
            new_hall = hall[:hall_spot] + (amphipod,) + hall[hall_spot+1:]

            room_steps = empty_spots + 1
            total_steps = room_steps + abs(hall_spot - room_doors[i])
            cost = total_steps * movement_cost[amphipod]
            total_cost = cost + solve(new_hall, new_rooms)

            best_cost = min(best_cost, total_cost)

    return best_cost

hall = ('.',) * 11
rooms = tuple(tuple(burrow[i][j + 1] for i in range(2, room_size + 2)) for j in room_doors)

print(solve(hall, rooms))
