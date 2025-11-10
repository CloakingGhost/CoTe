import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    x = int(input().rstrip())
    if x == 0:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
    else:
        element = (abs(x), x)
        heappush(heap, element)
