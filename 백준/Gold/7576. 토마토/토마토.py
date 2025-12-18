# https://www.acmicpc.net/problem/7576
# 토마토

from sys import stdin
from collections import deque

input = stdin.readline


def bfs1(matrix, tomatos, m, n):
    queue = deque(tomatos)
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    answer = 0
    while queue:
        i, j, count = queue.popleft()

        for d in range(4):
            nr, nc = dr[d] + i, dc[d] + j
            if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == 0:
                matrix[nr][nc] = 1
                queue.append((nr, nc, count + 1))

        if not queue:
            answer = count

    return -1 if any(c == 0 for r in matrix for c in r) else answer


def bfs2(matrix, tomatos, m, n):
    queue = deque(tomatos)
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    count = 0
    pointer = len(queue)
    while queue:
        i, j = queue.popleft()
        pointer -= 1

        for d in range(4):
            nr, nc = dr[d] + i, dc[d] + j
            if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == 0:
                matrix[nr][nc] = 1
                queue.append((nr, nc))
        if queue and pointer == 0:
            pointer = len(queue)
            count += 1

    return count


def bfs3(matrix, tomatos, m, n):
    queue = deque(tomatos)
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            nr, nc = dr[d] + i, dc[d] + j
            if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == 0:
                matrix[nr][nc] = matrix[i][j] + 1
                queue.append((nr, nc))

    ans = 0
    for row in matrix:
        if 0 in row:
            return -1
        ans = max(ans, max(row))
    return ans - 1


m, n = map(int, input().split())

matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]

# tomatos = [(i, j, 0) for i in range(n) for j in range(m) if matrix[i][j] == 1]
tomatos = [(i, j) for i in range(n) for j in range(m) if matrix[i][j] == 1]

print(bfs3(matrix, tomatos, m, n))
