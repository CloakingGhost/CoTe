from sys import stdin

input = stdin.readline


while True:
    line = None
    try:
        line = input()
        a, b = map(int, line.split())
        print(a + b)
    except:
        exit(0)
