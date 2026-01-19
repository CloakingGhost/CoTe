from sys import stdin

input = stdin.readline
N, M = map(int, input().split())

pocketmon = [input().rstrip() for _ in range(N)]
name_pocketmon = {name: i + 1 for i, name in enumerate(pocketmon)}
number_pocketmon = {i + 1: name for i, name in enumerate(pocketmon)}


for _ in range(M):
    command = input().rstrip()
    if command.isdigit():
        print(number_pocketmon[int(command)])
    else:
        print(name_pocketmon[command])
