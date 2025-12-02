import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0

for l in range(N - 2):
    if A[l] > 0:
        break

    m = l + 1
    r = N - 1
    while m < r:

        result = A[l] + A[m] + A[r]

        if result < 0:
            m += 1
        elif result > 0:
            r -= 1
        else:

            # 남은 구간 전체가 같은 값일 때
            if A[m] == A[r]:
                C = r - m + 1  # 조합
                count += C * (C - 1) // 2

                # 모든 경우를 계산했으므로 루프 종료
                break

            # 일반적인 중복 처리
            else:

                C_m = 1
                while A[m + C_m] == A[m]:
                    C_m += 1
                    
                C_r = 1
                while A[r - C_r] == A[r]:  
                    C_r += 1

                # 경우의 수 추가 
                count += C_m * C_r

                # 계산된 만큼 m과 r을 이동시켜 다음 중복되지 않는 쌍을 탐색
                m += C_m
                r -= C_r

print(count)