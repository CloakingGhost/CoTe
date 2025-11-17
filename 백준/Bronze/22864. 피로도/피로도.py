import sys

input = sys.stdin.readline

a, b, c, m = map(int, input().split())

time = 0  # 23까지
answer = 0  # b 영향
tired = 0  # a, c 영향


while time < 24:
    if tired + a <= m:
        tired += a
        answer += b
    else:
        if tired - c >= 0:
            tired -= c
        elif tired - c < 0:
            tired = 0
    time += 1
print(answer)