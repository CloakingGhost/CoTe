from sys import stdin

input = stdin.readline

X = int(input())
line = 1

# 1. 몇 번째 대각선 라인(line)에 있는지 찾기
# X가 현재 라인의 칸 수보다 크면, X에서 라인 수를 빼고 다음 라인으로 넘어감
while X > line:
    X -= line
    line += 1

# 2. 짝수 라인과 홀수 라인의 규칙 적용
# 짝수 라인 (2, 4, ...): 위에서 아래로(↘) 진행 -> 분자가 1부터 시작 (오름차순)
# 홀수 라인 (1, 3, ...): 아래에서 위로(↗) 진행 -> 분자가 line부터 시작 (내림차순)

if line % 2 == 0:
    a = X                # 분자
    b = line - X + 1     # 분모
else:
    a = line - X + 1     # 분자
    b = X                # 분모

print(f'{a}/{b}')