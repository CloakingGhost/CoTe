from sys import stdin


input = stdin.readline

P = int(input())
for p in range(1, P + 1):
    N, M = map(int, input().split())
    candidates = {input().rstrip(): 0 for _ in range(N)}
    for _ in range(M):
        X, R, C = input().rstrip().split()
        R = int(R)
        candidates[X] += R

    n, v = "", -1
    flag = False
    for name, vote in candidates.items():
        if vote == v:
            flag = True
            break
        elif vote > v:
            v = vote
            n = name
    if not flag :
        print(f"VOTE {p}: THE WINNER IS {n} {v}")
    else : 
        print(f"VOTE {p}: THERE IS A DILEMMA")
