from sys import stdin

input = stdin.readline
num = list(map(int, input().rstrip()))

num.sort(reverse=True)
for e in num:
    print(e, end="")
