from sys import stdin


input = stdin.readline

N = int(input())
for n in range(1, N + 1):
    equation = input().rstrip().split()

    a, b, c = int(equation[0][:-1]), int(equation[2]), int((equation[4]))

    print(f"Equation {n}")
    if a == 0 and c - b != 0:
        print("No solution.")
    elif a == 0 and c - b == 0:
        print("More than one solution.")
    else:
        val = (c - b) / a
        val = int(val * 1000000) / 1000000
        if val == 0:
            val = abs(val)
        print(f"x = {val:.6f}")
    print()
