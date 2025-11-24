import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline

# 1. 오버플로우 방지 2. 값 재사용
dp = [[0] * 30 for _ in range(30)]


def combinations(M, N):

    # 0! == 1
    if N == 0 or N == M:
        return 1

    # 1개만 뽑는 경우
    if N == 1 or N == M - 1:
        return M

    # 값 재사용
    if dp[M][N] != 0:
        return dp[M][N]

    # 조합, 재귀
    dp[M][N] = combinations(M - 1, N - 1) + combinations(M - 1, N)

    return dp[M][N]



T = int(input().strip())

for _ in range(T):

    line = input().strip()
    N, M = map(int, line.split())
    
    print(combinations(M, N))