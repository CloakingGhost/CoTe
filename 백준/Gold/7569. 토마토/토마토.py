# https://www.acmicpc.net/problem/7569
# 토마토

from collections import deque
from sys import stdin

input = stdin.readline
EMPTY, UNRIPE, RIPE = -1, 0, 1


def is_in_bounds(nh, nr, nc, max_h, n, m):
    return 0 <= nh < max_h and 0 <= nr < n and 0 <= nc < m


def has_unripe(matrix):
    return any(UNRIPE in r for h in matrix for r in h)


def bfs(tomatos, matrix, max_h, n, m):
    # 6방향
    dh, dr, dc = [0, 0, 0, 0, 1, -1], [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0]
    direction = len(dh)
    queue = deque(tomatos)
    result = 0
    while queue:
        h, r, c, t = queue.popleft()

        for d in range(direction):
            nh, nr, nc = h + dh[d], r + dr[d], c + dc[d]
            if is_in_bounds(nh, nr, nc, max_h, n, m) and matrix[nh][nr][nc] == UNRIPE:
                matrix[nh][nr][nc] = RIPE
                queue.append((nh, nr, nc, t + 1))

        if not queue:
            result = max(result, t)

    return -1 if has_unripe(matrix) else result

m, n, max_h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(max_h)]

TIME = 0
tomatos = [
    (i, j, k, TIME)
    for i in range(max_h)
    for j in range(n)
    for k in range(m)
    if matrix[i][j][k] == RIPE
]

print(bfs(tomatos, matrix, max_h, n, m))
