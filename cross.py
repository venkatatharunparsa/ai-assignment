from collections import deque

# Person time mapping
times = {'A': 5, 'B': 10, 'Gm': 20, 'Gf': 25}

# BFS search
def bridge_bfs():
    start = (frozenset(['A', 'B', 'Gm', 'Gf']), frozenset(), 'left', 0)
    queue = deque([start])
    visited = set()

    while queue:
        left, right, torch, time = queue.popleft()

        # Goal state: All on right
        if not left and torch == 'right' and time <= 60:
            return time

        if (left, right, torch, time) in visited:
            continue
        visited.add((left, right, torch, time))

        if torch == 'left':
            # Choose 1 or 2 from left to go right
            people = list(left)
            for i in range(len(people)):
                for j in range(i, len(people)):
                    group = {people[i]}
                    if i != j:
                        group.add(people[j])
                    new_left = left - group
                    new_right = right | group
                    new_time = time + max(times[p] for p in group)
                    queue.append((new_left, new_right, 'right', new_time))
        else:
            # One person returns to left with umbrella
            people = list(right)
            for person in people:
                new_left = left | {person}
                new_right = right - {person}
                new_time = time + times[person]
                queue.append((new_left, new_right, 'left', new_time))
    return -1

result_time = bridge_bfs()
print(f"\nMinimum time to cross the bridge: {result_time} minutes")