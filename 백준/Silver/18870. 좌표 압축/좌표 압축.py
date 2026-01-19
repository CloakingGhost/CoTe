from sys import stdin

input = stdin.readline
N = int(input())

sort_key = lambda x: (x[1], x[0])


coordinate = list(map(int, input().split()))

sorted_unique_coordinate = sorted(list(set(coordinate)))

rank_dict = {val: i for i, val in enumerate(sorted_unique_coordinate)}

print(*(rank_dict[x] for x in coordinate))
