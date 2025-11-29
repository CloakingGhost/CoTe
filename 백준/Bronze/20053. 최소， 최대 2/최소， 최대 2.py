import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, nums = int(input()), list(map(int, input().split()))
    print(min(nums), max(nums))