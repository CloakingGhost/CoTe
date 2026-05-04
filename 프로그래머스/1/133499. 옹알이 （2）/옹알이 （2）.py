def solution(babbling):
    sounds = ["aya", "ye", "woo", "ma"]
    answer = 0
    for b in babbling:
        for s in sounds:
            if s * 2 not in b:
                b = b.replace(s, " ")
        if b.isspace():
            answer += 1
    return answer