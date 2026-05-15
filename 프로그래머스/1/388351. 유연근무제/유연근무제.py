def solution(schedules, timelogs, startday):
    over_cnt = 0

    for i in range(len(schedules)):
        schedule: int = schedules[i] + 10  # 추가시간 10분
        timelog: list[int] = timelogs[i]
        isOver: bool = False
        # schedule 시간 올리기 / 1068 => 1108
        hour = schedule // 100 + schedule % 100 // 60
        minute = schedule % 100 % 60
        schedule = hour * 100 + minute

        for day in range(7):
            if (startday + day - 1) % 7 in [5, 6]:
                continue

            if timelog[day] > schedule:
                isOver = True
                break

        if isOver:
            over_cnt += 1

    return len(schedules) - over_cnt