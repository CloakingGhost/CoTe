import sys

# 문자열 입력 받기
s = sys.stdin.readline().strip()

stack = []  # 괄호의 유효성 검사 및 짝을 맞추기 위한 스택
answer = 0  # 최종 결과값 (덧셈 누적)
temp = 1    # 현재 괄호의 중첩 레벨에 따른 곱셈값 (분배법칙 적용)

# 문자열을 하나씩 순회
for i in range(len(s)):
    char = s[i]

    if char == '(':
        temp *= 2  # ( 괄호가 열리면 2를 곱해줌
        stack.append(char) # 스택에 괄호를 넣어 유효성 검사 준비

    elif char == '[':
        temp *= 3  # [ 괄호가 열리면 3을 곱해줌
        stack.append(char) # 스택에 괄호를 넣어 유효성 검사 준비

    elif char == ')':
        # 1. 스택이 비었거나, 2. 짝이 맞지 않으면 (예: '[)')
        # 즉시 0을 반환하고 종료해야 함
        if not stack or stack[-1] != '(':
            answer = 0
            break
        
        # 짝이 맞다면, 이전 문자를 확인
        # s[i-1] == '(' 는 "()" 케이스를 의미 (X가 없는 빈 괄호)
        if s[i-1] == '(':
            answer += temp  # 현재까지 누적된 곱셈값(temp)을 정답에 더해줌
        
        # ( 괄호를 스택에서 제거 (짝이 맞았으므로)
        stack.pop()
        # ) 괄호가 닫혔으므로, ( 열릴 때 곱했던 2를 다시 나눠줌 (레벨 복귀)
        temp //= 2

    elif char == ']':
        # 1. 스택이 비었거나, 2. 짝이 맞지 않으면 (예: '(]')
        if not stack or stack[-1] != '[':
            answer = 0
            break

        # 짝이 맞다면, 이전 문자를 확인
        # s[i-1] == '[' 는 "[]" 케이스를 의미 (X가 없는 빈 괄호)
        if s[i-1] == '[':
            answer += temp  # 현재까지 누적된 곱셈값(temp)을 정답에 더해줌
        
        # [ 괄호를 스택에서 제거 (짝이 맞았으므로)
        stack.pop()
        # ] 괄호가 닫혔으므로, [ 열릴 때 곱했던 3을 다시 나눠줌 (레벨 복귀)
        temp //= 3

# 루프가 정상적으로 끝났더라도, 스택에 괄호가 남아있다면
# (예: "(()" 또는 "([")
# 이는 올바르지 않은 괄호이므로 0을 출력
if stack:
    print(0)
else:
    # answer가 0으로 설정된 경우(break)도 여기서 0이 출력됨
    # 정상적으로 계산된 경우(예: 22)도 여기서 출력됨
    print(answer)