import sys


input = sys.stdin.readline


def move(d: int, board: list[list[int]], n: int):
    # 동
    if d == 0:
        # 행선택
        for i in range(n):
            # 각 열을 위한 pointer 설정
            pointer = n - 1
            # 열선택
            for j in range(n - 2, -1, -1):
                # 행열의 값이 0보다 큰경우만 진행
                if board[i][j] > 0:
                    tmp, board[i][j] = board[i][j], 0
                    ## 0이면 옮기기만 하면됨 아직 값이 더해질 수 있는 여지가 있음
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    ## 같으면 이동된 위치를 0 , pointer 위치의 값 *2, pointer-1
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer -= 1
                    ## 다르면 pointer-1, pointer 위치로 이동
                    else:
                        pointer -= 1
                        board[i][pointer] = tmp

    # 서
    elif d == 1:
        # 행선택
        for i in range(n):
            # 각 열을 위한 pointer 설정
            pointer = 0
            # 열선택
            for j in range(1, n):
                # 행열의 값이 0보다 큰경우만 진행
                if board[i][j] > 0:
                    tmp, board[i][j] = board[i][j], 0
                    ## 0이면 옮기기만 하면됨 아직 값이 더해질 수 있는 여지가 있음
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    ## 같으면 이동된 위치를 0 , pointer 위치의 값 *2, pointer-1
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer += 1
                    ## 다르면 pointer+1, pointer 위치로 이동
                    else:
                        pointer += 1
                        board[i][pointer] = tmp
    # 남
    elif d == 2:
        # 행선택
        for i in range(n):
            # 각 행을 위한 pointer 설정
            pointer = n - 1
            # 열선택
            for j in range(n - 2, -1, -1):
                # 행열의 값이 0보다 큰경우만 진행
                if board[j][i] > 0:
                    tmp, board[j][i] = board[j][i], 0
                    ## 0이면 옮기기만 하면됨 아직 값이 더해질 수 있는 여지가 있음
                    if board[pointer][i] == 0:
                        board[pointer][i] = tmp
                    ## 같으면 이동된 위치를 0 , pointer 위치의 값 *2, pointer-1
                    elif board[pointer][i] == tmp:
                        board[pointer][i] *= 2
                        pointer -= 1
                    ## 다르면 pointer-1, pointer 위치로 이동
                    else:
                        pointer -= 1
                        board[pointer][i] = tmp
    # 북
    elif d == 3:
        # 행선택
        for i in range(n):
            # 각 행을 위한 pointer 설정
            pointer = 0
            # 열선택
            for j in range(1, n):
                # 행열의 값이 0보다 큰경우만 진행
                if board[j][i] > 0:
                    tmp, board[j][i] = board[j][i], 0
                    ## 0이면 옮기기만 하면됨 아직 값이 더해질 수 있는 여지가 있음
                    if board[pointer][i] == 0:
                        board[pointer][i] = tmp
                    ## 같으면 이동된 위치를 0 , pointer 위치의 값 *2, pointer-1
                    elif board[pointer][i] == tmp:
                        board[pointer][i] *= 2
                        pointer += 1
                    ## 다르면 pointer+1, pointer 위치로 이동
                    else:
                        pointer += 1
                        board[pointer][i] = tmp

    return board


def merge_num(n: int, board: list[list[int]]):

    stack = [(board, 0)]

    max_num = 0
    while stack:
        board, cnt = stack.pop()
        if cnt == 5:
            max_num = max(max_num, *(e for r in board for e in r))
            continue

        for d in range(4):
            next_board = move(d, [r[:] for r in board], n)
            stack.append((next_board, cnt + 1))
    return max_num


n = int(input())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]

print(merge_num(n, board))
