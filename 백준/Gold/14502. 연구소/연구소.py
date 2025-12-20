# https://www.acmicpc.net/problem/14502
# 연구소

from sys import stdin
from collections import deque

input = stdin.readline
EMPTY, WALL, VIRUS = 0, 1, 2


def is_in_bounds(y, x, n, m):
    return 0 <= y < n and 0 <= x < m


def dfs(count, matrix, virus, empty_pos, start):

    if count == MAX_WALL_COUNT:
        return bfs(matrix, virus)

    max_safe_area = 0

    for i in range(start, EMPTY_COUNT):
        y, x = empty_pos[i]

        matrix[y][x] = WALL
        safe_count = dfs(count + 1, matrix, virus, empty_pos, i + 1)
        max_safe_area = max(max_safe_area, safe_count)
        matrix[y][x] = EMPTY

    return max_safe_area


def bfs(matrix, virus):
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    direction = len(dy)
    queue = deque(virus)
    tmp_matrix = [row[:] for row in matrix]

    virus_count = 0
    while queue:

        y, x = queue.popleft()
        for d in range(direction):
            ny, nx = y + dy[d], x + dx[d]
            if is_in_bounds(ny, nx, n, m) and tmp_matrix[ny][nx] == EMPTY:
                if tmp_matrix[ny][nx] == EMPTY:
                    tmp_matrix[ny][nx] = VIRUS
                    virus_count += 1
                    queue.append((ny, nx))

    return EMPTY_COUNT - virus_count - MAX_WALL_COUNT


n, m = map(int, input().split())
matrix = []
empty_pos = []
virus_pos = []

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    for j in range(m):
        if row[j] == EMPTY:
            empty_pos.append((i, j))
        elif row[j] == VIRUS:
            virus_pos.append((i, j))

WALL_COUNT_INIT = 0
MAX_WALL_COUNT = 3
EMPTY_COUNT = len(empty_pos)
print(dfs(WALL_COUNT_INIT, matrix, virus_pos, empty_pos, 0))
