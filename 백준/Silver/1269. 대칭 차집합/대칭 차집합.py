from sys import stdin

input = stdin.readline
A, B = map(int, input().split())

A_set = set(map(int, input().split()))
B_set = set(map(int, input().split()))
print(len(A_set | B_set) - len(A_set & B_set))
