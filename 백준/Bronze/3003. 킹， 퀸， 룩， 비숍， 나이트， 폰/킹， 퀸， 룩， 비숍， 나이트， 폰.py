from sys import stdin

input = stdin.readline


normal_piece = [1, 1, 2, 2, 2, 8]
piece = list(map(int, input().split()))
for i in range(6):
    piece[i] = normal_piece[i] - piece[i]
print(*piece)
