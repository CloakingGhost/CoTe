from sys import stdin

input = stdin.readline


N = int(input())

for i in range(1,10):
    print(f"{N} * {i} = {N * i}")