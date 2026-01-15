from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

bucket = [0] * (N + 1)
for _ in range(M):
    i, j, k = map(int, input().split())
    bucket[i : j + 1] = [k] * (j - i + 1)

print(*bucket[1:])
