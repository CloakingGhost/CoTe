from sys import stdin

input = stdin.readline


N = int(input())

nums = list(map(int, input().split()))
print(min(nums), max(nums))
