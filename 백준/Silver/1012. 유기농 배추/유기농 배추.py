import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x, y, ground, n, m):
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and ground[nx][ny]:
            ground[nx][ny] = 0
            dfs(nx, ny, ground, n, m)


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    ground = [[0] * m for _ in range(n)]
    bugs = 0
    for _ in range(k):
        x, y = map(int, input().split())
        ground[y][x] = 1

    for i in range(n):
        for j in range(m):
            if ground[i][j]:
                bugs += 1
                ground[i][j] = 0
                dfs(i, j, ground, n, m)

    print(bugs)