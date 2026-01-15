from sys import stdin

input = stdin.readline


N = int(input())
count = 0
for _ in range(N):
    word = input().rstrip()
    check_word = set()
    i = 0
    is_exist = False
    while i < len(word):
        w = word[i]

        if w in check_word:
            is_exist = True
            break

        for j in range(i + 1, len(word)):
            if w == word[j]:
                i = j
            else:
                check_word.add(w)
                break
        i += 1
    if not is_exist:
        count += 1

    # 글자 하나를 골라(인덱스)
    # set에 있는지 확인
    # 있으면 count 포함 x
    # 없으면 진행
    # 다음 글자가 고른 글자면 또 진행
    # 다음 글자가 고른 글자가 아니면 set 추가
    # 글자 하나를 골라


print(count)
