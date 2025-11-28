import sys

input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()
answer = (0, 0)


left, right = 0, n - 1
tmp = float("INF")
while left < right:
    current = solutions[left] + solutions[right]
    if abs(current) < tmp:
        tmp = abs(current)
        answer = (solutions[left], solutions[right])
    
    if current < 0:
        left += 1
    elif current > 0:
        right -= 1
    else:
        answer = (solutions[left], solutions[right])
        break
print(*answer)