import sys

input = sys.stdin.readline

# 입력
n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

q = int(input())
answer = []
for _ in range(q):
    t, k = map(int, input().split())
    # 단절점 - 루트, 리프 아니면 됨
    if t == 1:
        # 인접리스트에 담긴 노드 수 == 간선 수
        if len(graph[k]) == 1:
            answer.append("no")
        else:
            answer.append("yes")
    elif t == 2:
        answer.append("yes")
print("\n".join(answer))