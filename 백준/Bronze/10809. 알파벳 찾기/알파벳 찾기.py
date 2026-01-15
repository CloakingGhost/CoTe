from sys import stdin

input = stdin.readline
alphabet = [-1] * 26
S = input().rstrip()
for i in range(len(S)):
    idx = ord(S[i]) - 97
    if alphabet[idx] == -1:
        alphabet[idx] = i
print(*alphabet)
