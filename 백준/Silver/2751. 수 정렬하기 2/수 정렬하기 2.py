from sys import stdin

input = stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]

nums.sort()

for e in nums:
    print(e)
