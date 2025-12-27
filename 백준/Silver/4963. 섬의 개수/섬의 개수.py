# https://www.acmicpc.net/problem/4963
# 섬의 개수

from sys import stdin
from collections import deque

input = stdin.readline


def bfs(w, h, i, j, maps):
    dy, dx = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, 1, -1, 1, -1, 1, -1]
    queue = deque([(i, j)])
    maps[i][j] = 0
    while queue:
        y, x = queue.popleft()
        for d in range(8):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < h and 0 <= nx < w and maps[ny][nx]:
                maps[ny][nx] = 0
                queue.append((ny, nx))
                
    return 1


# 입력 마지막은 "0 0"
is_End = False
answer = []
while not is_End:
    command = input().rstrip()
    if command == "0 0":
        is_End = True
        break

    w, h = map(int, command.split())  # 지도 가로, 세로
    maps = [list(map(int, input().split())) for _ in range(h)]
    island = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j]:
                island += bfs(w, h, i, j, maps)

    answer.append(island)

    
for e in answer:
    print(e)