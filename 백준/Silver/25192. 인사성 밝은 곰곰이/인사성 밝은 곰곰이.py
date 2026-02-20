# https://www.acmicpc.net/problem/25192

import sys

input = sys.stdin.readline
N = int(input())
chat = set()

ans = 0

for _ in range(N):
    command = input().rstrip()

    if command == "ENTER":
        ans += len(chat)
        chat.clear()
    else:
        chat.add(command)  # 처음 채팅 입력하는 사람만 담음

ans += len(chat) # 새로운 사람이 들어온 이후 채팅하는 사람

print(ans)
