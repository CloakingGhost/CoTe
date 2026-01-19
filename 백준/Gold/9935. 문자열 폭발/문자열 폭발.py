from sys import stdin

input = stdin.readline
S, boom = input().rstrip(), input().rstrip()
boom_list = list(boom)
boom_len = len(boom_list)
last_char = boom[-1]
stack = []

for char in S:
    stack.append(char)

    # 마지막 단어가 boom의 마지막 문자
    # 최소 boom 길이 만큼 stack에 있어야 지울 수 있는 조건이 됨
    if char == last_char and len(stack) >= boom_len:
        # boom의 문자 길이 만큼 stack에 있으면 삭제
        if stack[-boom_len:] == boom_list:
            del stack[-boom_len:]

if stack:
    print("".join(stack))
else:
    print("FRULA")

"""
왜 stack 인가

문자열: CC44
boom : C4

입력값이 위와 같을 때 두번째 C 삽입 이후 4가 삽입되면 문제의 조건에 의해 문자열이 제거됨
이후 입력 문자열에서 두번째 4가 삽입되면 조건에 의해 제거 될 수 있음

이런 과정을 거칠 수 있는 자료구조는 스텍이 적절했음

이런 과정이라 함은 쌓여있는 값과 새로운 값을 조합해야 하는 상황을 뜻함
"""