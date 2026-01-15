from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
bucket = list(range(N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    bucket[i : j + 1] = bucket[i : j + 1][::-1]
print(*bucket[1:])
