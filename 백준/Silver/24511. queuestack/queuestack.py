from sys import stdin

input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))


queue_list = [B[i] for i in range(N) if A[i] == 0]
queue_list.reverse()
queue_list.extend(C)
print(*queue_list[:M])

"""
stack은 들어온 값이 바로 나가므로 무시
queue는 있던 값을 들어오면 0인덱스의 값을 밀어냄
A의 가장 끝 인덱스에 있던 값부터 출력
C는 0인덱스부터 입력값으로 들어감

따라서, A를 뒤집고 C를 확장하여 M 만큼 출력

"""