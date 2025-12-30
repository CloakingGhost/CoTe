from sys import stdin
input = stdin.readline
n = int(input())

# 방향 그래프
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
# 플로이드-워셜 방식 (핵심 로직 3줄)
for k in range(n):        # 거쳐가는 노드
    for i in range(n):    # 출발 노드
        for j in range(n):# 도착 노드
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for row in graph:
    print(*row)