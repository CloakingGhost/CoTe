# https://www.acmicpc.net/problem/4779

import sys


def change_black(dash, s, length):
    if length == 1:
        return

    sep = length // 3

    # 왼쪽
    change_black(dash, s, sep)
    # 중앙
    dash[s + sep : s + sep * 2] = [" "] * sep
    # 오른쪽
    change_black(dash, s + sep * 2, sep)


for line in sys.stdin:
    N = int(line)
    length = 3**N
    dash = ["-"] * length

    change_black(dash, 0, length)
    print("".join(dash))
