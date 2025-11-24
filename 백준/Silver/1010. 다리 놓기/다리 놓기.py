import sys

# 재귀 깊이 제한 설정 (N, M < 30 이므로 안전하게 설정)
sys.setrecursionlimit(5000) 
# 입력을 빠르게 처리하기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

# 전역 메모이제이션 테이블. 모든 테스트 케이스가 공유하며 재활용됩니다.
# (M, N의 최댓값이 29이므로 30x30 테이블 생성)
dp = [[0] * 30 for _ in range(30)]

def combinations(M, N):
    """
    재귀와 메모이제이션(DP)을 사용하여 MCN을 계산하는 함수
    """
    # 1. 기저 조건: N=0 또는 N=M인 경우
    if N == 0 or N == M:
        return 1
    
    # 2. 기저 조건: N=1 또는 N=M-1인 경우
    if N == 1 or N == M - 1:
        return M
        
    # 3. 메모이제이션: 이미 계산된 값이면 바로 반환
    if dp[M][N] != 0:
        return dp[M][N]
    
    # 4. 점화식 적용: DP(M, N) = DP(M-1, N-1) + DP(M-1, N)
    # 재귀 호출을 통해 값을 계산하고, DP 테이블에 저장
    # N은 M보다 작거나 같으므로, N=29, M=29까지 호출될 수 있음
    dp[M][N] = combinations(M - 1, N - 1) + combinations(M - 1, N)
    
    return dp[M][N]

def solve_per_line():
    """
    테스트 케이스를 한 줄씩 입력받아 즉시 계산하고 출력하는 함수
    """
    # 테스트 케이스 개수 T 입력
    try:
        T = int(input().strip())
    except:
        return

    # T번 반복하며 각 케이스를 즉시 처리
    for _ in range(T):
        try:
            line = input().strip()
            if not line:
                continue
            
            # N: 서쪽 사이트 개수, M: 동쪽 사이트 개수
            N, M = map(int, line.split())
            
            # N <= M 조건이 이미 주어져 있음
            if N > M:
                count = 0
            else:
                # 조합 함수 호출
                count = combinations(M, N)
            
            # 결과를 그때그때 출력합니다.
            print(count)
            
        except:
            # 입력 형식 오류 시 다음 케이스로 넘어감
            continue

# 함수 실행
solve_per_line()