import sys, math

input = sys.stdin.readline


# 팩토리얼로 구현
def bino_coef_factorial(n, k):
    return math.factorial(n - k) // math.factorial(k)


# 동적계획법: 한 문제를 작은 단위로 쪼개어 푸는 방법
## 부분적으로 동일한 연산이 반복되는 비효율이 있다
def bino_coef_as_is(n, k):
    if k == 0 or n == k:
        return 1
    return bino_coef_as_is(n - 1, k) + bino_coef_as_is(n - 1, k - 1)


## to be
## 한번 계산된 값을 저장
def bino_coef(n, r):
    # 1. 저장용 배열
    cache = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    # 2. 배열 초기화
    for i in range(n + 1):
        cache[i][0] = 1
    for i in range(r + 1):
        cache[i][i] = 1

    # 3. 연산
    for i in range(1, n + 1):
        for j in range(1, r + 1):
            cache[i][j] = cache[i - 1][j] + cache[i - 1][j - 1]

    return cache[n][r]


# 완전탐색
def bino_coef_prob(n, k):
    if k > n:
        return 0

    # 1.
    cache = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    # 2.
    def choose(times, got):
        # 3.
        if times == n:
            return got >= k

        # 4.
        if cache[times][got] != -1:
            return cache[times][got]

        # 5.
        cache[times][got] = 0.5 * choose(times + 1, got) + 0.5 * choose(
            times + 1, got + 1
        )
        return cache[times][got]

    # 6.
    return choose(0, 0)


print(bino_coef(*map(int, input().split())))
