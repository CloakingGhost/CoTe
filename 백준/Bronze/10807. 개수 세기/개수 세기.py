from sys import stdin

input = stdin.readline


N = int(input())
nums = list(map(int, input().split()))
v = int(input())
print(nums.count(v))
