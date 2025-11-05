import sys
from collections import deque

input = sys.stdin.readline


n = int(input())

queue = deque([])
for _ in range(n):
    command = input().rstrip()
    answer = 0
    if command == "size":
        print(len(queue))
    elif command == "pop":
        print(queue.popleft() if queue else -1)
    elif command == "empty":
        print(0 if queue else 1)
    elif command == "front":
        print(queue[0] if queue else -1)
    elif command == "back":
        print(queue[-1] if queue else -1)
    else:
        x = int(command.split()[1])
        queue.append(x)