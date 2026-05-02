# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check(room, n):
    room = [list(line) for line in room]
    for x in range(5):
        for y in range(5):

            if room[x][y] == "P":

                # 1차 델타 탐색
                for d_1 in range(4):
                    nx_1 = x + dx[d_1]
                    ny_1 = y + dy[d_1]
                    if 0 <= nx_1 < n and 0 <= ny_1 < n:

                        # 연속 "P"
                        if room[nx_1][ny_1] in "PA":
                            return 0

                        # 마킹
                        # 다음 P에서 델타탐색 중
                        # A를 발견하면 맨해튼 거리 2 안에 있음
                        elif room[nx_1][ny_1] == "O":
                            room[nx_1][ny_1] = "A"
    return 1


def solution(places):
    n = len(places)

    return [check(room, n) for room in places]