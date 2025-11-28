import sys

input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

left, right = 0, n - 1
best = 10**18
ans = (0, 0)

while left < right:
    s = solutions[left] + solutions[right]
    if abs(s) < best:
        best = abs(s)
        ans = (solutions[left], solutions[right])
    if s > 0:
        right -= 1
    else:
        left += 1

print(ans[0], ans[1])