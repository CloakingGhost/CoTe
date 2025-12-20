from sys import stdin
from collections import deque

input = stdin.readline
EMPTY, WALL, VIRUS = 0, 1, 2


def bfs(matrix, virus_pos, max_safe_count):
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = deque(virus_pos)
    tmp_matrix = [r[:] for r in matrix]
    potential_safe = INIT_EMPTY_COUNT - MAX_WALL_COUNT
    total_added_virus = 0
    while queue:
        y, x = queue.popleft()
        
        
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and tmp_matrix[ny][nx] == EMPTY:
                tmp_matrix[ny][nx] = VIRUS
                total_added_virus += 1
                queue.append((ny, nx))
                
                if potential_safe - total_added_virus <= max_safe_count:
                    return -1

    return potential_safe - total_added_virus


def dfs(wall_count, start):
    global max_safe_count

    if wall_count == MAX_WALL_COUNT:
        safe_count = bfs(matrix, virus_pos, max_safe_count)
        max_safe_count = max(max_safe_count, safe_count)
        return

    for i in range(start, INIT_EMPTY_COUNT):
        y, x = empty_pos[i]

        matrix[y][x] = WALL
        dfs(wall_count + 1, i + 1)
        matrix[y][x] = EMPTY


n, m = map(int, input().split())
empty_pos, virus_pos, matrix = [], [], []

MAX_WALL_COUNT = 3
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    for j in range(m):
        if row[j] == EMPTY:
            empty_pos.append((i, j))
        elif row[j] == VIRUS:
            virus_pos.append((i, j))

INIT_EMPTY_COUNT = len(empty_pos)
max_safe_count = 0
dfs(0, 0)
print(max_safe_count)