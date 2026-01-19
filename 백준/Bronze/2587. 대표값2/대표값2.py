from sys import stdin

input = stdin.readline


nums = [int(input()) for _ in range(5)]
nums.sort()
print(sum(nums) // len(nums))
print(nums[len(nums) // 2])
