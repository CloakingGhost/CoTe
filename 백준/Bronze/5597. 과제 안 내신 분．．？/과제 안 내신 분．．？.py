import sys

print(*sorted(set(range(1, 31)) - {int(sys.stdin.readline()) for _ in range(28)}), sep='\n')