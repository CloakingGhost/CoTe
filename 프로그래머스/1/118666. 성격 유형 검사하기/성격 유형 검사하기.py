def solution(survey, choices):
    # 유형별 점수
    scores = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0,
    }
    for i in range(len(survey)):
        category, choice = survey[i], choices[i]
        score = choice - 4
        # 음수면 앞쪽 유형
        if score < 0 :
            scores[category[0]] -= score
        # 양수면 뒤쪽 유형
        else :
            scores[category[1]] += score
    
    # 유형별 값 비교
    types = ["RT", "CF", "JM", "AN"]
    
    ## 출력부
    answer = ""
    for a_type, b_type in types:
        if scores[a_type] >= scores[b_type]:
            answer += a_type
        else:
            answer += b_type
            
    return answer