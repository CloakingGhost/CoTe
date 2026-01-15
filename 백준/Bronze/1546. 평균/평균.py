from sys import stdin

input = stdin.readline

N = int(input())
scores = list(map(float, input().split()))
M = max(scores)
new_scores = [scores[i] / M * 100 for i in range(N)]

print(sum(new_scores) / N)
