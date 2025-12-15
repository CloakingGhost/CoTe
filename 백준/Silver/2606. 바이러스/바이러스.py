def dfs(node):
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)

# 1. 그래프 구현
n, m = int(input()), int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# 2. 방문리스트
visited = [False] * (n + 1)

# 3. 깊이우선탐색 진행
visited[1] = True
dfs(1)

print(sum(visited) - 1)  # 1번 노드 제외