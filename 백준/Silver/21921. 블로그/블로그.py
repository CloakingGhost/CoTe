import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visited = list(map(int, input().split()))

left, right = -1, x - 1
temp = max_visited = sum(visited[:x])
cnt = 1

while right + 1 < n:
    left += 1
    right += 1

    temp -= visited[left]
    temp += visited[right]


    if max_visited < temp:
        max_visited = temp
        cnt = 1
    elif max_visited == temp:
        cnt += 1

if max_visited:
    print(max_visited)
    print(cnt)
else:
    print("SAD")