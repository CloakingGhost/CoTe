from sys import stdin

input = stdin.readline

max_num = -float("INF")
idx = 0
for i in range(9):
    num = int(input())
    if num > max_num:
        max_num = num
        idx = i
print(max_num)
print(idx + 1)
