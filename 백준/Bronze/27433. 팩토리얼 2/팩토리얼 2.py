import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)
dp[0] = 1

for n in range(1, N + 1):
    dp[n] = dp[n - 1] * n
print(dp[N])
