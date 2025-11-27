# https://www.acmicpc.net/problem/20922
# 겹치는 건 싫어
from collections import defaultdict
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
counter = defaultdict(int)

left, right = 0, 0
answer = 0
while right < n:
    if counter[numbers[right]] + 1 > k:
        answer = max(answer, sum(counter.values()))
        while counter[numbers[right]] + 1 > k:
            counter[numbers[left]] -= 1
            left += 1

    counter[numbers[right]] += 1
    right += 1

answer = max(answer, sum(counter.values()))

print(answer)
