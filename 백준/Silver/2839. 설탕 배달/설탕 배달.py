from sys import stdin

input = stdin.readline


N = int(input())
bags = 0
found = False
while N >= 0:
    if N % 5 == 0:
        bags += N // 5
        print(bags)
        found = True
        break

    N -= 3
    bags += 1

if not found:
    print(-1)
