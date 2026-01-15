from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

bucket = [i for i in range(N + 1)]
for _ in range(M):
    i, j = map(int, input().split())
    bucket[i], bucket[j] = bucket[j], bucket[i]
    # tmp = bucket[i]
    # bucket[i] = bucket[j]
    # bucket[j] = tmp

print(*bucket[1:])
