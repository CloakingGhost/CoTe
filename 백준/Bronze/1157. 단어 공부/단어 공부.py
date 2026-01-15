from sys import stdin

input = stdin.readline


S = input().rstrip().upper()
S_set = set(S)
S_dict = dict.fromkeys(S_set, 0)
max_frequency = 0
frequency_word = None

for s in S:
    S_dict[s] += 1
    if S_dict[s] > max_frequency:
        max_frequency = S_dict[s]
        frequency_word = s


print(frequency_word if list(S_dict.values()).count(max_frequency) == 1 else "?")
