# 로봇청소기 + 방의 상태(2차원 배열)
# 청소하는 영역의 개수 구하기

# n * m
# 청소기는 바라보는 방향이 있음
## 동서남북
## 처음에 빈칸은 전부 청소되지 않은 상태
# 벽 또는 빈 칸

# 현재 칸이 청소되지 않은경우 => 청소
# 현재 칸의 사방 중 청소되지 않은 빈 칸이 없는 경우(모두 청소가 된 경우)
## 바라보는 머리 방향 유지한 채로 한 칸 후진 => 처음로직 수행
## 후진 시 벽이면 작동 멈춤
# 현재 칸의 사방 중 청소되지 않은 칸이 있는 경우
## 반시계방향 90도 회전(좌회전)
## 회전 후 앞칸이 청소되지 않은 경우 전진 => 처음로직 수행


# 입력
## 1. 방 크기
## 2. 로봇청소기 위치(r, c)+ 로봇청소기의 머리방향 북동남서(0123)
## 3. 방 배열

# 한쪽 방향으로 진행하면 되므로 DFS
# 청소를 했어도 지나갈수 있으므로
# 편의적인 방식을 사용하기 위한 벽으로 변환하면 안됨
## 청소 여부를 bool으로 별도 관리
import sys

input = sys.stdin.readline

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]  # 북동남서
TYPE, CONDITION = 0, 1  # key
WALL, IS_CLEAN = 1, False  # value


def dfs(cr, cc, head):
    clean_count = 0
    # 현재 칸이 청소되지 않은 경우
    if not room[cr][cc][CONDITION]:
        room[cr][cc][CONDITION] = True
        clean_count += 1

    # 현재 칸의 사방 중 (청소할 빈 칸 찾는 로직)
    ## 반시계 회전
    for _ in range(4):
        ## 이동 후보
        head = (head + 3) % 4
        nr, nc = cr + dr[head], cc + dc[head]
        # 앞칸이 벽이 아니고 청소되지 않은 경우 전진
        if room[nr][nc][TYPE] != WALL and not room[nr][nc][CONDITION]:
            ## 청소 완료하면 청소한 칸 갯수 추가
            ### return을 해줘야 재귀에서 돌아왔을 때 다른 방향으로 안가고
            ### 방청소 했던 결과만 추가해서 호출위치로 돌아감
            return clean_count + dfs(nr, nc, head)

    # 사방이 청소가 됐다면(for문을 통과했다면)
    ## 바라보는 머리 방향 유지한 채로 한 칸 후진 가능한지 확인
    move_d = (head + 2) % 4
    nr, nc = cr + dr[move_d], cc + dc[move_d]
    ## 후진 시 벽이면 작동 멈춤
    if room[nr][nc][TYPE] == WALL:
        return clean_count
    ## 머리 방향 유지한 채로 후진
    ### 이동 후 청소 완료하면 청소한 칸 갯수 추가
    return clean_count + dfs(nr, nc, head)


n, m = map(int, input().split())
r, c, head = map(int, input().split())
room = [list(map(lambda x: [int(x), IS_CLEAN], input().split())) for _ in range(n)]


print(dfs(r, c, head))
