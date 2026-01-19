from sys import stdin

input = stdin.readline
S = input().rstrip()

substrings = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        substrings.add(S[i : j + 1])
print(len(substrings))
