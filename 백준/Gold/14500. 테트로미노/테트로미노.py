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
    paper: list[list[int]],
    visited: list[list[bool]],
):
    global max_num
    if count == 4 : 
        if sum_paper_num > max_num:
            max_num = sum_paper_num
        return

    for d in range(4):
        nr, nc = current_r + dr[d], currnet_c + dc[d]
        if paper[nr][nc] and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(sum_paper_num + paper[nr][nc], count + 1, nr, nc, paper, visited)
            visited[nr][nc] = False


# 입력
n, m = map(int, input().split())
paper = [[0] * (m + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    paper[i][1 : m + 1] = list(map(int, input().split()))
visited = [[False] * (m + 2) for _ in range(n + 2)]
max_num = -1
for r in range(1, n + 1):
    for c in range(1, m + 1):
        up, down, left, right = (
            paper[r - 1][c],
            paper[r + 1][c],
            paper[r][c - 1],
            paper[r][c + 1],
        )
        up_block = up + left + right + paper[r][c]
        down_block = down + left + right + paper[r][c]
        left_block = left + up + down + paper[r][c]
        right_block = right + up + down + paper[r][c]
        # r, c / r - 1, c / r + 1, c / r, c - 1 / r, c + 1
        max_num = max(max_num, up_block, down_block, left_block, right_block)
for r in range(1, n + 1):
    for c in range(1, m + 1):
        visited[r][c] = True
        dfs(paper[r][c], 1, r, c, paper, visited)
        visited[r][c] = False
print(max_num)
