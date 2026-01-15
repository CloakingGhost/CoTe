from sys import stdin

input = stdin.readline


N, X = map(int, input().split())
nums = list(map(int, input().split()))
print(*filter(lambda num: num < X, nums))
