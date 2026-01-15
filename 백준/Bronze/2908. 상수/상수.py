from sys import stdin

input = stdin.readline


print(max(int(num[::-1]) for num in input().rstrip().split()))
