# keymap을 한번에 조회하도록 만들어야 함
# key들을 한번씩은 조회하고 최소 인덱스를 별도의 배열에 저장
def solution(keymap, targets):
    # [keymap_idx, char_idx]
    keylist = [(101, 101)] * 26

    # 키맵에서 문자열꺼내
    # 문제열에서 문자꺼내
    # 그 문자의 인덱스를 별도의 배열에 저장할건데
    # 지금 문자의 인덱스가 별도 배열에 저장된 인덱스보다 작으면 교체
    # 배열을 찾아갈 때는 ord(문자) -65을 하면 인덱스가 나옴

    for i, key in enumerate(keymap):
        for j, k in enumerate(key):
            if j < keylist[ord(k) - 65][1]:
                keylist[ord(k) - 65] = (i, j + 1)

    answer = []
    for t in targets:
        count = 0
        for c in t:
            keymap_idx, char_idx = keylist[ord(c) - 65]
            if keymap_idx != 101:
                count += char_idx
            else:
                count = -1
                break
        answer.append(count)
    return answer