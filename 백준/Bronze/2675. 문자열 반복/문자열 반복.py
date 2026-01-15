from sys import stdin

input = stdin.readline

T = int(input())

for _ in range(T):
    R, S = input().rstrip().split()

    print("".join(s * int(R) for s in S))

# 각 자리에서 하나씩 뽑아
# 뽑은 것을 R 만큼 반복하여 문자열 생성
