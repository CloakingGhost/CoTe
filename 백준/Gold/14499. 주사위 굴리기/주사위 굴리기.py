import sys

input = sys.stdin.readline

# n * m 지도
# 오른쪽 동쪽 // 위쪽 북쪽

# 지도 위에 주사위
## 주사위 전개도 등장
## 가장 처음에 주사위에는 모든 면에 0

# 지도에는 각 칸에 정수가 있다
# 지도 위에서 주사위를 굴렸는데
# 지도 위 칸에 수가 0인 위치에 주사위가 있으면
# 주사위 바닥면에 있는 수가 지도의 칸으로 복사

# 지도 위 칸에 수가 0이 아니면
# 지도 위의 수가 주사위에 바닥면으로 복사 되고
# 지도의 칸은 0이 됨

# 주의
# 주사위가 지도를 벗어나면 명령, 출력 무시
# 처음 주사위는 모든 면이 0
# 주사위를 놓은 칸에 쓰여 있는 수는 항상 0

n, m, dice_r, dice_c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
############
# dice = [[0] * m for _ in range(n)]  # 주사위 바닥면 관리 # 불필요
# dice_top = deque([0, 0]) # 불필요
dice = [0] * 6  # 0: 밑 / 1: 앞 / 2: 좌 / 3: 뒤 / 4: 우 / 5: 상
############
commands = tuple(map(lambda x: int(x) - 1, input().split()))
# 동서북남 // 동쪽은 0, 서쪽은 1, 북쪽은 2, 남쪽은 3
dr, dc = [0, 0, -1, 1], [1, -1, 0, 0]


def roll(command, dice):
    if command == 0:
        dice[5], dice[2], dice[0], dice[4] = dice[2], dice[0], dice[4], dice[5]
    elif command == 1:
        dice[5], dice[2], dice[0], dice[4] = dice[4], dice[5], dice[2], dice[0]
    elif command == 2:
        dice[5], dice[3], dice[0], dice[1] = dice[1], dice[5], dice[3], dice[0]
    elif command == 3:
        dice[5], dice[3], dice[0], dice[1] = dice[3], dice[0], dice[1], dice[5]

    """
    직관적으로 관리를 해야한다는 것을 떠올리지 못했음
    deque, 2차원 주사위 배열 등등 필요 없고 직관적으로 하는 것이 좋음
    """


for command in commands:

    # 명령어 방향으로 주사위 굴리기
    ndr, ndc = dice_r + dr[command], dice_c + dc[command]

    ## 경계 확인
    if not (0 <= ndr < n and 0 <= ndc < m):
        continue

    ## 주사위 이동
    dice_r, dice_c = ndr, ndc

    ## 주사위 굴리기
    roll(command, dice)

    # 보드 바닥확인
    ## 0이 아니면
    if board[dice_r][dice_c]:
        # 보드의 숫자를 주사위 바닥면에 넣고
        dice[0] = board[dice_r][dice_c]
        ## 보드 0으로 변경
        board[dice_r][dice_c] = 0
    ## 0이면
    else:
        ## 주사위 바닥면 숫자를 보드에 넣기
        board[dice_r][dice_c] = dice[0]

    # 주사위 윗면 출력
    print(dice[5])
