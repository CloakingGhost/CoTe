# https://www.acmicpc.net/problem/1764
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
hearing_set = {input().rstrip() for _ in range(n)}
seeing_set = {input().rstrip() for _ in range(m)}


answer = hearing_set & seeing_set
answer = sorted(answer)

print(len(answer))
print("\n".join(answer))
