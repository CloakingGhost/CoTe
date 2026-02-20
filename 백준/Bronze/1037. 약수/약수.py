# https://www.acmicpc.net/problem/1037

import sys

input = sys.stdin.readline

amount = int(input())
nums = list(map(int, input().split()))

nums.sort()

print(nums[0]*nums[-1])