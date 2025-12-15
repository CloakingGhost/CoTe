# https://www.acmicpc.net/problem/9372
# 상근이의 여행

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    stack = [1]
    visited = [False] * (n+1)
    visited[1] = True
    count = 0
    while stack:
        node = stack.pop()
        for next_node in graph[node]:
            if not visited[next_node]:
                stack.append(next_node)
                visited[next_node] = True
                count += 1
                
    print(count)
        
    