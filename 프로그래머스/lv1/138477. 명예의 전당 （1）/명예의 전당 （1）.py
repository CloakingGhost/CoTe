from heapq import heappop, heappush
def solution(k, score):
    answer = []
    heap = []
    for points in score:
        heappush(heap, points)
        
        if len(heap) > k:
            heappop(heap)
            
        answer.append(heap[0])
    return answer