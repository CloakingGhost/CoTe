def sieve_of_eratosthenes(n: int = 3000):
    numbers = [True] * (n + 1)
    numbers[0] = False
    numbers[1] = False
    for i in range(2, n + 1):
        if numbers[i]:
            for j in range(i + i, n + 1, i):
                numbers[j] = False
    return numbers


def solution(nums):
    answer = 0
    primes = sieve_of_eratosthenes()

    def combination():
        nonlocal answer
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    num = nums[i] + nums[j] + nums[k]
                    if primes[num]:
                        answer += 1

    # combination()
    visited = [False] * len(nums)

    def dfs_combination(curr: int, num: int, depth: int):
        result = 0

        if depth == 3:
            if primes[num]:
                return 1
            return 0

        for next_idx in range(curr + 1, len(nums)):
            if not visited[next_idx]:
                visited[next_idx] = True
                result += dfs_combination(next_idx, num + nums[next_idx], depth + 1)
                visited[next_idx] = False

        return result

    for i in range(len(nums)):
        visited[i] = True
        answer += dfs_combination(i, nums[i], 1)
        visited[i] = False

    return answer