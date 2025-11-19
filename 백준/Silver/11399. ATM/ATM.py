import sys

input = sys.stdin.readline
    
N = int(input())
P = list(map(int, input().rstrip().split()))

# 오름차순 정렬
P.sort()

# 총 대기 시간의 합
total_time = 0
# 누적 시간
current_wait = 0 

for time in P:
    # 돈 인출 '총 시간'
    current_wait += time 
    
    # 이 '총 시간'을 전체 시간의 합에 누적
    total_time += current_wait
    
print(total_time)