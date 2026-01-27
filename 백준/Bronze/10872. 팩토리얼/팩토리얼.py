import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    dp[i] = dp[i - 1] * i
print(dp[N])
