import sys

input = sys.stdin.readline

# n개의 시험장
# i번 시험장에 A_i명

# 감독관
## 1. 총감독관 : B명 관리 가능
## 2. 부감독관 : C명 관리 가능

# 총감독관은 시험장 마다 1명
# 부감독관은 시험장 마다 여려명 가능

# 모든 응시생을 감시해야함
# 감독관 수의 최솟값


# 1개의 시험장에 필요한 감독관 수 * n
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
proctors = 0

for examinee in a:
    proctor = 1
    tmp = examinee
    tmp -= b
    
    if tmp > 0:
        proctor += tmp // c
        tmp %= c

        if tmp:
            proctor += 1
    proctors += proctor


print(proctors)
