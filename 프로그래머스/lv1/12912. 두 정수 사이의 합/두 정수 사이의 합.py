def solution(a, b):
    s = min(a, b)
    e = max(a, b)
    answer = 0
    for n in range(s, e + 1):
        answer += n
    
    return answer