import sys
from heapq import heappop, heappush
from collections import defaultdict # defaultdict를 사용하면 키 존재 여부 체크 불필요

input = sys.stdin.readline
T = int(input())  # 테스트 케이스

for _ in range(T):
    k = int(input())
    max_heap = []
    min_heap = []
    # 이 딕셔너리가 핵심입니다.
    # 각 숫자가 현재 큐에 몇 개 있는지 카운트합니다.
    is_valid = defaultdict(int) 
    
    for _ in range(k):
        command, n = input().split()
        n = int(n)

        if command == "I":
            heappush(max_heap, -n)
            heappush(min_heap, n)
            is_valid[n] += 1  # n이라는 숫자가 1개 추가되었음을 기록
        
        elif command == "D":
            if n == 1:  # 최댓값 삭제
                # '유효한' 최댓값을 찾을 때까지 힙에서 제거합니다.
                # 힙이 비어있지 않고, 힙의 top이 유효하지 않은 값(0)이라면
                while max_heap and is_valid[-max_heap[0]] == 0:
                    heappop(max_heap) # 유령 데이터(이미 삭제된 값) 버리기
                
                if max_heap: # 버릴게 다 버려지고 힙에 유효한 값이 남았다면
                    valid_max = -heappop(max_heap) # 진짜 최댓값을 꺼냄
                    is_valid[valid_max] -= 1 # 유효 카운트 1 감소
                    
            elif n == -1: # 최솟값 삭제
                # '유효한' 최솟값을 찾을 때까지 힙에서 제거합니다.
                while min_heap and is_valid[min_heap[0]] == 0:
                    heappop(min_heap) # 유령 데이터 버리기

                if min_heap:
                    valid_min = heappop(min_heap) # 진짜 최솟값을 꺼냄
                    is_valid[valid_min] -= 1 # 유효 카운트 1 감소

    # 모든 연산이 끝난 후, 힙에 유령 데이터만 남아있을 수 있으므로
    # 마지막으로 힙을 정리합니다.
    while max_heap and is_valid[-max_heap[0]] == 0:
        heappop(max_heap)
    while min_heap and is_valid[min_heap[0]] == 0:
        heappop(min_heap)

    # 최종 결과 출력
    if not max_heap or not min_heap: # 둘 중 하나라도 비어있으면 큐는 비어있음
        print("EMPTY")
    else:
        print(-max_heap[0], min_heap[0]) # 유효한 최댓값과 최솟값 출력