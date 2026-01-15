from sys import stdin

input = stdin.readline


while True:
    line = input().rstrip()
    if line:
        print(line)
    else:
        break
