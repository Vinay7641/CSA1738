from collections import deque
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
queue = deque([(start, [])])
visited = {start}
while queue:
    state, path = queue.popleft()
    if state == goal:
        for step in path + [state]:
            print(step[:3])
            print(step[3:6])
            print(step[6:])
            print()
        break
    zero = state.index(0)
    for move in [-3, 3, -1, 1]:
        new = zero + move
        if 0 <= new < 9 and not (
            move == -1 and zero % 3 == 0
        ) and not (
            move == 1 and zero % 3 == 2
        ):
            s = list(state)
            s[zero], s[new] = s[new], s[zero]
            s = tuple(s)
            if s not in visited:
                visited.add(s)
                queue.append((s, path + [state]))
