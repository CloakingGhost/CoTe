import sys

input = sys.stdin.readline
n = int(input())
count = 0
cows = [-1] * (n + 1)
for _ in range(n):
    cow, status = map(int, input().split())
    if cows[cow] == -1:
        cows[cow] = status
        
    if cows[cow] != -1 and cows[cow] != status:
        count += 1
    cows[cow] = status

print(count)