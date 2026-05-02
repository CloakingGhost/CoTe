def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []
    for move in moves:
        for i in range(n):
            doll_num = board[i][move - 1]
            if doll_num:
                board[i][move - 1] = 0
                if stack and stack[-1] == doll_num:
                    stack.pop()
                    answer += 2
                    break
                stack.append(doll_num)
                break

    return answer