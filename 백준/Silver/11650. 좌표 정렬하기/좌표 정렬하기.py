from sys import stdin

input = stdin.readline
N = int(input())

sort_key = lambda x: (x[0], x[1])


coordinate = [tuple(map(int, input().split())) for _ in range(N)]
coordinate.sort(key=sort_key)

for e in coordinate:
    print(*e)