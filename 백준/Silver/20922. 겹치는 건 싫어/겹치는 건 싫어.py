from collections import defaultdict
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
counter = defaultdict(int)

left = 0
answer = 0

for right, val in enumerate(numbers):
    counter[val] += 1
    while counter[val] > k:
        counter[numbers[left]] -= 1
        left += 1
    answer = max(answer, right - left + 1)

print(answer)