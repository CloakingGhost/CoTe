# keymap을 한번에 조회하도록 만들어야 함
# key들을 한번씩은 조회하고 최소 인덱스를 별도의 dict에 저장
def solution(keymap, targets):
    keydict = {}

    # 키맵에서 문자열꺼내
    # 문자열에서 문자꺼내
    # dict에 문자가 없거나 인덱스가 더 작으면 인덱스 + 1 저장 

    for key in keymap:
        for i, c in enumerate(key):
            if c not in keydict or i + 1 < keydict[c]:
                keydict[c] = i + 1

    answer = []
    
    for t in targets:
        count = 0
        for c in t:
            if c not in keydict:
                count = -1
                break

            count += keydict[c]

        answer.append(count)
    return answer