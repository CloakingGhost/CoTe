from sys import stdin

input = stdin.readline

A, B, V = map(int, input().split())


V -= A
day = V // (A - B)

if V % (A - B):
    day += 1

print(day + 1)
