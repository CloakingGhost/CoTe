from sys import stdin

input = stdin.readline


S = input().rstrip()
total = 0
for s in S:
    distance = (ord(s) - 65) // 3

    if distance == 6:
        if s == "S":
            distance = 5
    elif distance == 7:
        if s == "V":
            distance = 6
    elif distance > 7:
        distance = 7
    total += distance + 3

print(total)

# abc = 0 => 3
# def = 1(distance) => 3 + 1(distance)
# ghi = 2
# jkl = 3
# mno = 4
# pqrs = 5
# tuv = 6
# wxyz = 7
