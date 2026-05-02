from collections import Counter

def solution(s):
    return "".join(sorted([ key for key, count in Counter(s).items() if count == 1 ]))