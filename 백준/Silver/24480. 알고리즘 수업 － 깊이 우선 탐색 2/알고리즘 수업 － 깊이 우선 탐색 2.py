# https://www.acmicpc.net/problem/24480
# 알고리즘 수업 - 깊이 우선 탐색 2

import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for edge in graph:
    edge.sort()

count = 1
stack = [r]
answer = [0] * (n + 1)

while stack:
    node = stack.pop()
    
    if answer[node] == 0:
        answer[node] = count
        count += 1

        for next_node in graph[node]:
            if answer[next_node] == 0:
                stack.append(next_node)

for ans in answer[1:]:
    print(ans)
