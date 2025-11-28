import sys

input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))
left = 0
odd = 0
answer = 0

for right in range(n):
    odd += nums[right] & 1
    while odd > k:  # 홀수를 줄여야 하기 때문에 줄어드는 부분까지 left 이동
        odd -= nums[left] & 1
        left += 1
    answer = max(right - left + 1 - odd, answer)

print(answer)