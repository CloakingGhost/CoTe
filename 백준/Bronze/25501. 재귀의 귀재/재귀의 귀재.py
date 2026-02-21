import sys

input = sys.stdin.readline

T = int(input())


def recursion(s, count, l, r):
    if l >= r:
        return (1, count)
    elif s[l] != s[r]:
        return (0, count)
    return recursion(s, count + 1, l + 1, r - 1)


def is_palindrome(s):
    return recursion(s, 1, 0, len(s) - 1)


for _ in range(T):
    print(*is_palindrome(input().rstrip()))
