import sys

input = sys.stdin.readline

N, K = map(int, input().split())

MOD = 1_000_000_000
dp = [[1] * (N + 1) for _ in range(K + 1)]

for k in range(2, K + 1):
    for n in range(1, N + 1):
        prevN = dp[k][n - 1]
        prevK = dp[k - 1][n]

        dp[k][n] = (prevN + prevK) % MOD

print(dp[K][N])