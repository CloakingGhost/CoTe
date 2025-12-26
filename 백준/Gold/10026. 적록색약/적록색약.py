# https://www.acmicpc.net/problem/10026
# 적록색약

from sys import stdin
from collections import deque

input = stdin.readline
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(cy, cx, color, is_color_blind):
    visited[cy][cx] = True
    queue = deque([(cy, cx)])

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if is_color_blind:
                    if color in "RG" and colors[ny][nx] in "RG":
                        queue.append((ny, nx))
                        visited[ny][nx] = True
                    else:
                        if color == colors[ny][nx]:
                            queue.append((ny, nx))
                            visited[ny][nx] = True
                else:
                    if colors[ny][nx] == color:
                        queue.append((ny, nx))
                        visited[ny][nx] = True

    return 1


n = int(input())

colors = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


answer = [0, 0]  # 정상, 색맹(빨 == 초)


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            answer[0] += bfs(i, j, colors[i][j], False)
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            answer[1] += bfs(i, j, colors[i][j], True)

print(*answer)
