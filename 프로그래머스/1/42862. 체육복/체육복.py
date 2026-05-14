def solution(n, lost, reserve):
    # 여분이 있는 학생 중 잃어버린 학생
    # 이 학생은 본인것은 있기에 참여 가능

    # 여분이 있는 학생중 도난당한 학생
    # 진짜 빌려줄수 있는 학생 번호
    real_reserve = set(reserve) - set(lost)

    # 여분의 체육복조차 없는 학생
    real_lost = set(lost) - set(reserve)

    for s in list(real_reserve):

        # 앞번호 학생
        if s - 1 in real_lost:
            real_lost.remove(s - 1)  # s - 1 번호 학생은 체육복이 생김

        # 뒷번호 학생
        elif s + 1 in real_lost:
            real_lost.remove(s + 1)
            
    return n - len(real_lost)

