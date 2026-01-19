from sys import stdin

input = stdin.readline

N, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
print(x[-k])
