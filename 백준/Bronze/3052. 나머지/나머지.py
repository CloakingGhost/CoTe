from sys import stdin

input = stdin.readline

answer = set()
for _ in range(10):
    answer.add(int(input()) % 42)
print(len(answer))
