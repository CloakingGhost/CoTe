import sys

n = int(sys.stdin.readline())

MAX_NUM = 1_100_000

is_prime = [True] * (MAX_NUM + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX_NUM**0.5) + 1):
    if is_prime[i]:
        # i*i 부터 i의 배수들을 모두 False로 변경
        for j in range(i * i, MAX_NUM + 1, i):
            is_prime[j] = False


def is_palindrome(num_str):
    return num_str == num_str[::-1]


for num in range(n, sys.maxsize):
    if is_prime[num] and is_palindrome(str(num)):
        print(num)
        break