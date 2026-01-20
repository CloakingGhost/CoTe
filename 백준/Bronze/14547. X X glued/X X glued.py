from sys import stdin
from collections import deque

input = stdin.readline

while True:
    line = input().rstrip()
    if line == "#":
        break
    a, b, c = line.split()
    queue = deque(b)

    answer = []
    while len(queue) > 1:
        char = queue.popleft()
        if char == queue[0]:
            answer.append(int(char))
            queue.popleft()

    unique_answer = set(answer)
    if answer:
        if len(unique_answer) > 1:
            print(
                "{} {} glued and {} {} glued".format(
                    answer[0], answer[0], answer[1], answer[1]
                )
            )
        else:
            print("{} {} glued".format(answer[0], answer[0]))
