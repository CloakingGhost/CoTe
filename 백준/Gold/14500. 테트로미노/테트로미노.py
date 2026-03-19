# n * m 종이
# 숫자가 쓰여있는 종이 위에
## 숫자는 1~1000 자연수
# 테트로미노를 1개 놓았을 때 그 수의 최대합

# 사방탐색(꼭지점끼리 연결불가)
# 테트로미노는 정사각형 4개로 이뤄짐
## 방향전환 가능 => 방향의 제약 없음
# BFS: 목적지까지 갔다가 돌아와서 다른 방향으로 가야함(stack)
## 해당 방향으로 탐색을 마치면 visited를 풀어줘야 함
### 그래야 다른 경우에 탐색이 가능

# 글로벌 최대값

# T자 모양 테트로미노를 어떻게 구현하는지가 관건
import sys


# 세팅
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

## 우하좌상
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]


def dfs(
    sum_paper_num: int,
    count: int,
    current_r: int,
    currnet_c: int,
):
    global max_num

    # 가지치기(ver.3)
    # 남은 길을 최대값으로 가정하고 진출할 경우
    # max_num 보다 작거나 같다면 더이상 진행하지 않음
    ## 즉, max_num 보다 큰 값을 기대할 수 없는 경우
    # if sum_paper_num + max_val * (4 - count) <= max_num:
    #     return

    if count == 4:
        max_num = max(max_num, sum_paper_num)
        return

    for d in range(4):
        nr, nc = current_r + dr[d], currnet_c + dc[d]
        if paper[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = True

            # T 블록 탐색(ver.3)
            ## 다음 위치로 넘기지 않고 현재위치에서 탐색하도록 진행
            ## 현 위치 값 + 다음위치 값 + 그 외 나머지 2칸을 탐색하게 됨
            if count == 2:
                dfs(sum_paper_num + paper[nr][nc], count + 1, current_r, currnet_c)

            dfs(sum_paper_num + paper[nr][nc], count + 1, nr, nc)
            visited[nr][nc] = False


# 입력
n, m = map(int, input().split())
paper = [[0] * (m + 2) for _ in range(n + 2)]
max_val = -1
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    paper[i][1 : m + 1] = row
    max_val = max(max_val, max(row))
    
visited = [[False] * (m + 2) for _ in range(n + 2)]
max_num = -1

# T자 블럭(ver.1)
# for r in range(1, n + 1):
#     for c in range(1, m + 1):
#         up, down, left, right = (
#             paper[r - 1][c],
#             paper[r + 1][c],
#             paper[r][c - 1],
#             paper[r][c + 1],
#         )
#         up_block = up + left + right + paper[r][c]
#         down_block = down + left + right + paper[r][c]
#         left_block = left + up + down + paper[r][c]
#         right_block = right + up + down + paper[r][c]
#         # r, c / r - 1, c / r + 1, c / r, c - 1 / r, c + 1
#         max_num = max(max_num, up_block, down_block, left_block, right_block)

for r in range(1, n + 1):
    for c in range(1, m + 1):
        # T자 블럭(ver.2)
        # adjacent = [paper[r - 1][c], paper[r + 1][c], paper[r][c - 1], paper[r][c + 1]]
        # max_num = max(paper[r][c] + sum(adjacent) - min(adjacent), max_num)

        # 나머지 블럭
        visited[r][c] = True
        dfs(paper[r][c], 1, r, c)
        visited[r][c] = False

print(max_num)
