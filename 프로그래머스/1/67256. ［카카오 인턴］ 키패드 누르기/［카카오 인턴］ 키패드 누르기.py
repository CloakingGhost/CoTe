def solution(numbers, hand):
    # 상수
    L, R = "L", "R"
    row, col = 0, 1
    ## 왼쪽 세로 키패드
    left_side = [1, 4, 7]
    ## 오른쪽 세로 키패드
    right_side = [3, 6, 9]

    # 왼손잡이, 오른손잡이 구분
    standard = L if hand == "left" else R
    # 엄지 시작위치
    l_pos, r_pos = [3, 0], [3, 2]

    # 오른쪽 세로 키패드

    answer = []

    # 좌표
    def get_pos(num):
        return [(num - 1) // 3, (num - 1) % 3] if num != 0 else [3, 1]

    for num in numbers:
        if num in left_side:
            answer.append(L)
            l_pos = get_pos(num)
        elif num in right_side:
            answer.append(R)
            r_pos = get_pos(num)
        else:
            num_pos = get_pos(num)
            l_distance = abs(l_pos[row] - num_pos[row]) + abs(l_pos[col] - num_pos[col])
            r_distance = abs(r_pos[row] - num_pos[row]) + abs(r_pos[col] - num_pos[col])

            if l_distance < r_distance:
                l_pos = num_pos
                answer.append(L)
            elif l_distance > r_distance:
                r_pos = num_pos
                answer.append(R)
            else:
                if standard == L:
                    l_pos = num_pos
                else:
                    r_pos = num_pos
                answer.append(standard)

    return "".join(answer)