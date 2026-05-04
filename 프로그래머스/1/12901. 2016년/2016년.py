from datetime import date
def solution(a, b):
    # SUN,MON,TUE,WED,THU,FRI,SAT
    days = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    day = date(2016, a, b)

    return days[day.weekday()]