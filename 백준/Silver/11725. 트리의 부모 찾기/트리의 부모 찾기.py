import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [False] * (n + 1)
parent = [0] * (n + 1) # visited 대용
stack = [1]

while stack :
    current_node = stack.pop()

    for next_node in graph[current_node]:
        # 부모를 아직 지정 않했으면
        if parent[next_node] == 0:
        # next_node의 부모인 current_node 지정
            parent[next_node] = current_node
        # 다음 노드 stack에 추가
            stack.append(next_node)

# 2번 노드부터 출력(문제의 조건)
for num in parent[2:]:
    print(num)