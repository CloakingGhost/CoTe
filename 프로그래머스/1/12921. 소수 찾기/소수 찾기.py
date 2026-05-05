def sieve_of_eratosthenes(n: int = 2):
    numbers = [True] * (n + 1)
    numbers[0] = False
    numbers[1] = False
    for i in range(2, n + 1):
        if numbers[i]:
            for j in range(i + i, n + 1, i):
                numbers[j] = False
    return numbers


def solution(n):
    answer = 0
    primes = sieve_of_eratosthenes(n)
    for i in range(n + 1):
        if primes[i]:
            answer += 1
    return answer
