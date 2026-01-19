from sys import stdin

input = stdin.readline

N = int(input())

nums = [0] * 10001

for _ in range(N):
    num = int(input())
    nums[num] += 1

for i in range(len(nums)):
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)
