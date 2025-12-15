# https://www.acmicpc.net/problem/1260
# DFS와 BFS

import sys
from collections import deque

input = sys.stdin.readline


def dfs(node, visited, answer):
    answer.append(node)
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, visited, answer)


def bfs(node):
    answer = []
    queue = deque([node])
    visited = [False] * (n + 1)
    visited[node] = True

    while queue:
        current_node = queue.popleft()
        answer.append(current_node)
        for next_node in graph[current_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

    return answer


n, m, v = map(int, input().split())  # vertax, edge, start node

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for edge in graph:
    edge.sort()

answer_dfs = []
dfs(v, [False] * (n + 1), answer_dfs)
answer_bfs = bfs(v)

print(*answer_dfs)
print(*answer_bfs)
