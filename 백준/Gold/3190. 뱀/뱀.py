import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
k = int(input())

# n * n // 2는 벽 // 외벽 생성: 조건문 간소화
board = [[2] * (n + 2) for _ in range(n + 2)]

# 빈 땅
for i in range(1, n + 1):
    board[i][1 : n + 1] = [0] * n

# 사과
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1

# 전환 명령어
l = int(input())

commands = {
    int(x): (c, 1 if c == "D" else -1)
    for x, c in (input().rstrip().split() for _ in range(l))
}

# 초기 세팅
time = 0
snake = deque([(1, 1)])
board[1][1] = 2  # 몸을 벽과 동일 취급

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]  # 우하좌상 : 우측 전진 초기값
direction = 0

while True:
    time += 1
    hr, hc = snake[-1]  # head row, head column
    nr, nc = hr + dr[direction], hc + dc[direction]
    # 벽 혹은 몸에 충돌 시 종료
    if board[nr][nc] == 2:
        break

    if board[nr][nc] == 0:  # 빈 땅이라면
        tr, tc = snake.popleft()
        board[tr][tc] = 0  # 꼬리위치 제거

    snake.append((nr, nc))
    board[nr][nc] = 2  # 뱀으로 바꿈

    # 방향 전환 확인
    if time in commands:
        command, d = commands[time]
        direction = (direction + d) % 4

print(time)


# 사과위치는 어떻게 확인하지?
## 보드에 사과를 깔아두고 뱀이 지나가면 지우자
## 뱀은 계속 이동하고 배열로 위치와 길이가 관리가 가능하기 때문에
## 사과 관리를 위해 보드에 깔아야 함
# 보드를 채워야 하나? 뱀은 가상으로 사과는 보드에
## 보드는 외벽을 임의로 만들어서 조건문을 간소화 하자
# 방향 조작은 dx, dy로 만들어서 명령어가 나올 때 가감 나머지 연산자 활용 필요
## 4 + -1 % 4 : 이걸로 마이너스 대응
### 파이썬은 음수 나눗셈 문제 없음
## 3 + 1 % 4 : 이걸로 리스트 범위에러 대응
# 뱀은 어떻게 관리하지? => 큐 1초마다 변경
## 보드에도 몸통을 추가 해야 했음....*****
# 뱀의 머리가 다음 진행 방향에서 어디에 있나 1초마다 확인
# 언제까지???
## 종료 조건까지 반복