from sys import stdin

input = stdin.readline
N, M = map(int, input().split())

S = {input().rstrip(): 0 for _ in range(N)}
for _ in range(M):
    valid_str = input().rstrip()

    if S.get(valid_str) != None:
        S[valid_str] += 1

print(sum(S.values()))
