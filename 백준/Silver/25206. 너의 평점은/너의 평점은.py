from sys import stdin

input = stdin.readline

level_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
total_score = 0.0
total_level = 0.0
for _ in range(20):
    subject, point, level = input().rstrip().split()

    if level != "P":
        total_score += level_score[level] * float(point)
        total_level += float(point)

print(total_score / total_level if total_level else total_score)
