from sys import stdin

input = stdin.readline


N = int(input())
for i in range(N):
    for j in range(i, N - 1):
        print(" ", end="")
    for j in range(2 * (i + 1) - 1):
        print("*", end="")
    print()
for i in range(N - 2, -1, -1):
    for j in range(i, N - 1):
        print(" ", end="")
    for j in range(2 * (i + 1) - 1):
        print("*", end="")
    print()
