from sys import stdin

input = stdin.readline

N = int(input())
nums = list(input().rstrip())
total = 0
for num in nums:
    total += int(num)
print(total)