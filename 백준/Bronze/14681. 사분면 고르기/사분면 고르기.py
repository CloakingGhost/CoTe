from sys import stdin

input = stdin.readline


def find_quadrant(x, y):
    if x > 0:
        if y > 0:
            return 1
        else:
            return 4
    else:
        if y > 0:
            return 2
        else:
            return 3


x, y = int(input()), int(input())


print(find_quadrant(x, y))
