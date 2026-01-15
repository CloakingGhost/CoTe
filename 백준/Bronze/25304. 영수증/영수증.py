from sys import stdin

input = stdin.readline


X = int(input())  # 총액
N = int(input())  # 물건 종류

total = 0
for _ in range(N):
    a, b = map(int, input().split())
    total += a * b
    
print("Yes" if X == total else "No")
