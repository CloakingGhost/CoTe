# https://www.acmicpc.net/problem/7569
# 토마토

from collections import deque
from sys import stdin

input = stdin.readline


def is_in_area(nh, nr, nc, max_h, n, m):
    return 0 <= nh < max_h and 0 <= nr < n and 0 <= nc < m


def bfs(tomatos, matrix, max_h, n, m):
    # 6방향
    dh, dr, dc = [0, 0, 0, 0, 1, -1], [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0]
    queue = deque(tomatos)
    result = 0
    while queue:
        h, r, c, t = queue.popleft()

        for d in range(6):
            nh, nr, nc = h + dh[d], r + dr[d], c + dc[d]
            if is_in_area(nh, nr, nc, max_h, n, m) and matrix[nh][nr][nc] == 0:
                matrix[nh][nr][nc] = 1
                queue.append((nh, nr, nc, t + 1))

            if not queue:
                result = t

    return -1 if any(0 in r for h in matrix for r in h) else result

# max_h 재할당 방지
m, n, max_h = map(int, input().split())
matrix = [[list(map(int, input().split())) for _ in range(n)] for _ in range(max_h)]

tomatos = [
    (i, j, k, 0)
    for i in range(max_h)
    for j in range(n)
    for k in range(m)
    if matrix[i][j][k] == 1
]

print(bfs(tomatos, matrix, max_h, n, m))
