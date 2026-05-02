from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for s, e in edge:
        graph[e].append(s)
        graph[s].append(e)

    distance = [-1] * (n + 1)
    distance[1] = 0
    queue = deque([1])
    
    while queue:
        current_node = queue.popleft()
        
        for next_node in graph[current_node]:
            if distance[next_node] == -1:
                distance[next_node] = distance[current_node] + 1
                queue.append(next_node)
                
    max_distance = max(distance)

    return distance.count(max_distance)