import sys

input = sys.stdin.readline
t = int(input())
dp = [[0] * 30 for _ in range(30)]


def combinations(m, n):
    if n == 0 or n == m:
        return 1
    if n == 1 or n == m - 1:
        return m
    if dp[m][n]:
        return dp[m][n]

    dp[m][n] = combinations(m - 1, n - 1) + combinations(m - 1, n)
    
    return dp[m][n]


for _ in range(t):
    n, m = map(int, input().split())

    print(combinations(m, n))