from sys import stdin

input = stdin.readline

units = [25, 10, 5, 1]
T = int(input())

for _ in range(T):
    N = int(input())
    change = []

    for unit in units:
        change.append(N // unit)
        N %= unit

    print(*change)
