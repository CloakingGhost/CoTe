from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
dq = deque([])
for _ in range(N):
    line = input().rstrip().split()
    command = int(line[0])
    if command == 1:
        dq.appendleft(int(line[1]))
    elif command == 2:
        dq.append(int(line[1]))

    elif command == 3:
        if dq:
            print(dq.popleft())
        else:
            print(-1)

    elif command == 4:
        if dq:
            print(dq.pop())
        else:
            print(-1)

    elif command == 5:
        print(len(dq))
    elif command == 6:
        if dq:
            print(0)
        else:
            print(1)
    elif command == 7:
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif command == 8:
        if dq:
            print(dq[-1])
        else:
            print(-1)
