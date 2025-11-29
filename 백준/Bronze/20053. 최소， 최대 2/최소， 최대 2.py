import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, nums = int(input()), sorted(list(map(int, input().split())))
    print(nums[0], nums[-1])
