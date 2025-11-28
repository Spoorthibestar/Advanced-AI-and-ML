import time
from collections import deque

W, H = 5, 5
obstacles = {(1, 1), (2, 4), (3, 4)}
tasks = {(0, 2), (2, 1), (3, 0)}
agent = (0, 0)

def bfs(start, goal):
    q = deque([(start, [start])])
    seen = {start}
    while q:
        (x, y), path = q.popleft()
        if (x, y) == goal:
            return path
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in obstacles and (nx, ny) not in seen:
                q.append(((nx, ny), path + [(nx, ny)]))
                seen.add((nx, ny))
    return None

def cell(x, y):
    if (x, y) == agent:
        return "A"
    if (x, y) in tasks:
        return "T"
    if (x, y) in obstacles:
        return "X"
    return "."

def show():
    print("\n".join(" ".join(cell(x, y) for y in range(H)) for x in range(W)))
    print()
    time.sleep(0.5)

print("Initial Board")
show()

while tasks:
    paths = [(bfs(agent, t), t) for t in tasks if bfs(agent, t)]
    path, goal = min(paths, key=lambda p: len(p[0]))
    for agent in path[1:]:
        show()
    print(f"Picked task at {goal}\n")
    tasks.remove(goal)

print("Agent finished work")
