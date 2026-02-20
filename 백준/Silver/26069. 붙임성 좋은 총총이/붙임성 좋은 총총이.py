from sys import stdin

input = stdin.readline

N = int(input())

meet = set()
findChongChong = False
for _ in range(N):
    A, B = input().rstrip().split()
    if not findChongChong and (A == "ChongChong" or B == "ChongChong"):
        findChongChong = True
        meet.add(A)
        meet.add(B)

    if findChongChong:
        if A in meet or B in meet:
            meet.add(A)
            meet.add(B)

print(len(meet))