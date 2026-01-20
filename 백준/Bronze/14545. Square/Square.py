from sys import stdin


input = stdin.readline

P = int(input())


for _ in range(P):
    N = int(input())
    answer = 0
    for i in range(1, N + 1):
        answer += i * i
    print(answer)
