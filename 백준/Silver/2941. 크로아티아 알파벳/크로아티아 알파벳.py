from sys import stdin

input = stdin.readline


S = input().rstrip()


croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
for c in croatia:
    S = S.replace(c, "*")

print(len(S))
