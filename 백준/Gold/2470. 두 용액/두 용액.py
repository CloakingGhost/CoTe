import sys

input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

left, right = 0, n - 1
tmp = float("INF")
answer = (0, 0)

while left < right:
    current = solutions[left] + solutions[right]
    if abs(current) < tmp:
        tmp = abs(current)
        answer = (solutions[left], solutions[right])
        if current == 0:
            break
    
    if current < 0:
        left += 1
    else:
        right -= 1

print(*answer)