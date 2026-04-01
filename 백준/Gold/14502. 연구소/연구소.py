# n * m 연구소
# 빈칸, 벽, 바이러스
# 새로운 벽을 반드시 3개 세워야 함
# 안전 영역 최댓값 구하기

import sys

input = sys.stdin.readline


def spread_virus(board):
    new_virus = 0
    stack = virus_position[:]
    init_empty = len(empty_position) - WALL * 3
    while stack:
        r, c = stack.pop()

        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == EMPTY:
                board[nr][nc] = VIRUS
                new_virus += 1
                stack.append((nr, nc))

                # 가지치기
                ## 현재까지 계산된 안전영역의 수가
                ## 최대 안전영역 수보다 작은경우
                ## 탐색을 더 진행하는 것은 비효율
                if init_empty - new_virus <= max_safety_area:
                    return -1

    return init_empty - new_virus


def make_wall(count, start):
    global max_safety_area

    # for의 개수
    if count == 3:
        tmp_board = [row[:] for row in board]
        safety_count = spread_virus(tmp_board)
        max_safety_area = max(max_safety_area, safety_count)
        # 종료
        return

    # 탐색(조합)의 형태
    for i in range(start, len(empty_position)):
        r, c = empty_position[i]
        board[r][c] = WALL
        make_wall(count + 1, i + 1)
        board[r][c] = EMPTY


dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
n, m = map(int, input().split())
EMPTY, WALL, VIRUS = 0, 1, 2
board = []
empty_position = []
virus_position = []
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(m):
        if row[j] == VIRUS:
            virus_position.append((i, j))
        elif row[j] == EMPTY:
            empty_position.append((i, j))

max_safety_area = 0

make_wall(0, 0)

print(max_safety_area)


# empty_position을 반복문을 돌리는 것으로 로직 시작
# board를 copy한다.
# 벽을 세운다
## 벽은 안전영역에 세운다
### 안전영역을 처음에 따로 모은다
### BFS를 사용해서 조합을 구현
### visited는 board 자체가 된다.
# 바이러스를 퍼뜨린다
## 바이러스는 사방으로 퍼진다
## 퍼지는 방식은 DFS, BFS 상관없음
### 바이러스가 퍼진 수를 세어서 안전영역에서 뺄 수 있도록 변수 설정
### 가지치기 : 바이러스의 수가 현재까지 계산된 안전영역의 수보다 더 적어질 수 있는 경우 더이상 탐색하지 않음
### 현재까지 바이러스 수를 안전영역에서 뺀 결과가 현재까지 계산된 안전영역의 최대수 보다 큰 경우 더이상 탐색하지 않음
# 안전영역을 센다
## 새로 생긴 바이러스 수만큼 뺀다


# max_safety_area = 0
# for i in range(len(empty_position)):
#     ir, ic = empty_position[i]
#     for j in range(i + 1, len(empty_position)):
#         jr, jc = empty_position[j]
#         for k in range(j + 1, len(empty_position)):
#             tmp_board = [row[:] for row in board]
#             kr, kc = empty_position[k]
#             tmp_board[ir][ic] = WALL
#             tmp_board[jr][jc] = WALL
#             tmp_board[kr][kc] = WALL

#             new_virus = 0
#             for vr, vc in virus_position:
#                 new_virus += spread_virus(tmp_board, vr, vc)
#             safety_area = len(empty_position) - new_virus - (WALL * 3)
#             max_safety_area = max(max_safety_area, safety_area)
# print(max_safety_area)
