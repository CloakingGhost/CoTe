from sys import stdin

input = stdin.readline
N = int(input())

sort_key = lambda x: (int(x[1]), x[0])


coordinate = [(i, *input().split()) for i in range(N)]
coordinate.sort(key=sort_key)

for e in coordinate:
    print(*e[1:])
