import sys
from collections import deque

input = sys.stdin.readline

def bfs(N):
    queue = deque([(N, 0)])
    # visited[i] : 숫자 i에 도달했는지 여부 (중복 방지)
    # N+1 크기의 배열을 만들어 O(1)로 접근
    visited = [False] * (N + 1)
    visited[N] = True
    
    while queue:
        n, cnt = queue.popleft()
        
        if n == 1:
            return cnt
        
        # 3가지 경우의 수를 모두 확인 (순서대로 넣으면 큐 특성상 BFS 유지)
        
        # 1. 3으로 나누기
        if n % 3 == 0 and not visited[n // 3]:
            visited[n // 3] = True
            queue.append((n // 3, cnt + 1))
            
        # 2. 2로 나누기
        if n % 2 == 0 and not visited[n // 2]:
            visited[n // 2] = True
            queue.append((n // 2, cnt + 1))
            
        # 3. 1 빼기 (항상 가능)
        if n - 1 >= 1 and not visited[n - 1]:
            visited[n - 1] = True
            queue.append((n - 1, cnt + 1))

print(bfs(int(input())))