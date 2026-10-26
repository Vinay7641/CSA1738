from collections import deque
start = (3, 3, 0)
goal = (0, 0, 1)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
q = deque([(start, [])])
visited = set()
while q:
    (m, c, boat), path = q.popleft()
    if (m, c, boat) == goal:
        for step in path + [(m, c, boat)]:
            print(step)
        break
    if (m, c, boat) in visited:
        continue
    visited.add((m, c, boat))
    for x, y in moves:
        nm = m - x if boat == 0 else m + x
        nc = c - y if boat == 0 else c + y
        if not (0 <= nm <= 3 and 0 <= nc <= 3):
            continue
        rm, rc = 3 - nm, 3 - nc
        if (nm == 0 or nm >= nc) and (rm == 0 or rm >= rc):
            state = (nm, nc, 1 - boat)
            if state not in visited:
                q.append((state, path + [(m, c, boat)]))
