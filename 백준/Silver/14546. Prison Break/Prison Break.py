from sys import stdin
from collections import deque

input = stdin.readline

P = int(input())

dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]

for _ in range(P):
    L, W, A, B, C, D = map(int, input().split())
    labyrinth = [list(input().rstrip()) for _ in range(W)]
    labyrinth.reverse()
    queue = deque([(B - 1, A - 1)])

    hut = labyrinth[B - 1][A - 1]
    labyrinth[B - 1][A - 1] = ""
    answer = "NO"
    while queue:
        b, a = queue.popleft()

        if b == D - 1 and a == C - 1:
            answer = "YES"
            break
        for d in range(4):
            nb, na = dr[d] + b, dc[d] + a

            if 0 <= nb < W and 0 <= na < L and labyrinth[nb][na] == hut:
                labyrinth[nb][na] = ""
                queue.append((nb, na))
    print(answer)
