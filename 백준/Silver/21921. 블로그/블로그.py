import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visited = list(map(int, input().split()))

current = max_visited = sum(visited[:x])
count = 1

for i in range(x, n):

    current += visited[i] - visited[i - x]

    if max_visited < current:
        max_visited = current
        count = 1
    elif max_visited == current:
        count += 1

if max_visited:
    print(max_visited)
    print(count)
else:
    print("SAD")
