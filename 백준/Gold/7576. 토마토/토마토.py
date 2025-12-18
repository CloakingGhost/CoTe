import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(box, tomatos, n, m):
    queue = deque(tomatos)
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

    while queue:
        x, y, t = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = 1
                queue.append((nx, ny, t + 1))

    return -1 if any(box[i][j] == 0 for i in range(n) for j in range(m)) else t


m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]

tomatos = [(i, j, 0) for i in range(n) for j in range(m) if box[i][j] == 1]

print(dfs(box, tomatos, n, m))