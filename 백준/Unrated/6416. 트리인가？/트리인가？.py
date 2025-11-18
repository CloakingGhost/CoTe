import sys
from collections import defaultdict, deque

# 입력을 편하게 받기 위한 제너레이터 함수
# 공백과 줄바꿈에 상관없이 숫자들을 하나씩 꺼내줍니다.
def input_generator():
    for line in sys.stdin:
        for token in line.split():
            yield int(token)

def solve():
    # 1. 초기화
    tokens = input_generator()
    case_num = 1
    
    # 그래프 정보를 담을 자료구조
    adj = defaultdict(list)   # 인접 리스트 (u -> v)
    indegree = defaultdict(int) # 진입 차수 (노드로 들어오는 간선의 개수)
    nodes = set()             # 존재하는 모든 노드의 집합

    while True:
        try:
            # 스트림에서 u, v 두 개의 숫자를 가져옴
            u = next(tokens)
            v = next(tokens)
        except StopIteration:
            break

        # 종료 조건
        if u == -1 and v == -1:
            break
        
        # 케이스 종료 및 판별 시작 (0 0)
        if u == 0 and v == 0:
            is_tree = True
            
            # [예외 처리] 노드가 하나도 없는 경우도 트리로 간주 (문제 조건)
            if len(nodes) == 0:
                print(f"Case {case_num} is a tree.")
            else:
                # [검증 1] 루트 노드 찾기 및 진입 차수 검사
                root_count = 0
                root_node = -1
                
                for node in nodes:
                    # 들어오는 간선이 없는 노드가 루트 후보
                    if indegree[node] == 0:
                        root_count += 1
                        root_node = node
                    # 루트가 아닌데 들어오는 간선이 1개가 아니라면(2개 이상) 트리가 아님
                    elif indegree[node] > 1:
                        is_tree = False
                        break
                
                # 루트가 정확히 1개가 아니면 트리가 아님
                if root_count != 1:
                    is_tree = False
                
                # [검증 2] 연결성 확인 (BFS 탐색)
                # 위 조건들을 통과했더라도, 루트와 연결되지 않은 '분리된 사이클'이 존재할 수 있음
                if is_tree:
                    queue = deque([root_node])
                    visited_count = 0
                    visited = {root_node} # 중복 방문 방지 (무한 루프 방지)

                    while queue:
                        curr = queue.popleft()
                        visited_count += 1
                        
                        for next_node in adj[curr]:
                            # 트리라면 자식 노드로 가는 길은 유일해야 하므로, 이미 방문한 곳을 또 가면 안 됨
                            if next_node in visited:
                                is_tree = False
                                break
                            visited.add(next_node)
                            queue.append(next_node)
                        if not is_tree: break
                    
                    # 탐색이 끝난 후, 방문한 노드 개수가 전체 노드 개수와 다르면
                    # (즉, 루트에서 갈 수 없는 노드가 존재하면) 트리가 아님
                    if is_tree and visited_count != len(nodes):
                        is_tree = False

                # 결과 출력
                if is_tree:
                    print(f"Case {case_num} is a tree.")
                else:
                    print(f"Case {case_num} is not a tree.")

            # 다음 케이스를 위해 변수 초기화
            adj.clear()
            indegree.clear()
            nodes.clear()
            case_num += 1
        
        else:
            # 간선 정보 저장
            adj[u].append(v)
            indegree[v] += 1 
            # indegree 딕셔너리에 u가 없으면 0으로 초기화 (출발 노드도 기록하기 위함)
            if u not in indegree:
                indegree[u] = 0
            
            nodes.add(u)
            nodes.add(v)

if __name__ == "__main__":
    solve()