import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = list(map(int, input().rstrip().split()))

for _ in range(m):
    command, a, b = map(int, input().split())
    a = a - 1
    if command == 1:
        s[a] = b
    elif command == 2:
        s[a:b] = [x ^ 1 for x in s[a:b]]
    elif command == 3:
        s[a:b] = [0] * (b - a)
    elif command == 4:
        s[a:b] = [1] * (b - a)
        
print(*s)