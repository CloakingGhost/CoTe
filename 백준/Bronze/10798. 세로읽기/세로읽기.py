from sys import stdin

input = stdin.readline

matrix = [[""] * 15 for _ in range(5)]

for i in range(5):
    row = list(input().rstrip())
    matrix[i][: len(row)] = row
    
answer = []
for i in range(15):
    for j in range(5):
        if matrix[j][i]:
            answer.append(matrix[j][i])
print("".join(answer))