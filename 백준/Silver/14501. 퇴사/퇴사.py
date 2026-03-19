# 시작일을 일자별로 부터 시작했을 때로 반복문 시작
# 첫 인덱스 부터 선택
# 선택 후 기간이 최대 일을 넘어가는지 확인
# 넘어가지 않으면 일 진행 후
# 보수금 추가 + 날짜 건너뛰기

# 최대 금액 비교하며 갱신

# 구조
# for + while(날짜 건너뛰기가 필요함)
# 즉 브루트포스

# 건너뛰고 다시 탐색

# 문제 상황 발생
# 10
# 5 50
# 4 40
# 3 30
# 2 20
# 1 10
# 1 10
# **2 20** : 이부분을 건너뛰지 못함
# 3 30
# 4 40
# 5 50

# 이전 단계에서 탐색 후에 다시 경우의 수를 세어야 함
# 이 문제에서 경우에 수는 k일을 건너뛴 경우 최대 보수가 얼마나 되는가

import sys

input = sys.stdin.readline
n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n)]

max_price = 0

# 출근 시작일로 부터 업무 처리 후
# 다시 출근 할 때 퇴사 일 전까지 건너 뛰고
# 출근하는 경우를 구현 해야 함


def bfs(day, price):
    global max_price
    if day >= n:  # 퇴사기간이라면
        max_price = max(max_price, price)
        return
    t, p = schedule[day]
    if day + t - 1 < n:  # 오늘 포함 퇴사 전날까지 일할 분량인가
        price += p
        for i in range(day + t - 1, n):
            bfs(i + 1, price)  # i일의 다음 날


for i in range(n):
    bfs(i, 0)

print(max_price)
