from sys import stdin

input = stdin.readline
N = int(input())
sanggun = list(map(int, input().rstrip().split()))

M = int(input())
nums = {val: 0 for val in map(int, input().rstrip().split())}

for s in sanggun:
    if nums.get(s) != None:
        nums[s] += 1
print(*nums.values())
