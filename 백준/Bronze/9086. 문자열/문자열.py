from sys import stdin

input = stdin.readline

T = int(input())
for _ in range(T):
    S = input().rstrip()
    print(f"{S[0]}{S[-1]}")
