import sys, math

input = sys.stdin.readline

N = int(input())


def change_blank(matrix, x, y, length):
    if length == 1:
        return
    step = length // 3
    for i in range(x, x + length, step):
        for j in range(y, y + length, step):
            if i == x + step and j == y + step:
                for k in range(i, i + step):
                    for l in range(j, j + step):
                        matrix[k][l] = " "
            else:
                change_blank(matrix, i, j, step)


def change_blank_refactor(matrix, x, y, length):
    if length == 1:
        return
    
    step = length // 3

    for i in range(x, x + length, step):
        for j in range(y, y + length, step):
            if i == x + step and j == y + step:
                for k in range(i, i + step):
                    matrix[k][j : j + step] = [" "] * step
            else:
                change_blank(matrix, i, j, step)

matrix = [["*"] * N for _ in range(N)]

change_blank_refactor(matrix, 0, 0, N)

print('\n'.join([''.join(row) for row in matrix]))


"""
문제 이해
1. 삼각형 별찍기 문제처럼 한 줄씩 즉석에서 출력하면 안될 것이라는 걸 느낌
2. 반복적인 패턴이 보이므로 함수도 반복적으로 실행해서 모양을 만들어야 함을 알 수 있음
3. 즉, 재귀를 사용해 종료조건을 만들어야 했음

아이디어
1. 빈 배열에서 조건을 통해 "*", " " 값을 배열에 추가
2. 영역을 나눌 수 있는 기준을 찾아 재귀 수행
3. 입력값 크기만큼 배열을 준비하고 뭔지 모를 작업 수행
4. "*" 배열 또는 " " 배열을 미리 준비하여 작업 수행

아이디어 종합 결론
1. 특정 조건에 가운데 부분을 빈 공간으로 바꾼다.
2. 나머지 영역에 대해 재귀 호출을 통해 빈 공간으로 바꾼다.


필요한 값
1. 영역 분할 기준
2. 재귀 수행 조건
3. 빈 공간으로 바꾸는 방법
4. 빈 공간을 얼마나 바꿔야 하는지 기준
5. 종료 조건

도출 과정
1. 정사각형의 크기는 (N/3)*(N/3)이기에 9등분 할 수 있다.
2. 9개로 나뉜 영역을 재귀 호출하지만 가운데 영역은 예외
3. 9개 영역 탐색의 출발점으로 부터 (x, y) 둘 다 9의 영역을 나누는 기준(length // 3) 만큼 떨어진 곳에 도달
4. 영역을 나누는 기준 만큼 빈공간으로 교체(length // 3)
5. 탐색해야 하는 영역의 크기가 1*1이면 종료(정사각형이므로 길이 값 1개만 전달)
"""
