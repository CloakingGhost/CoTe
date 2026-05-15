def solution(new_id: str):
    # 1. 소문자로 치환
    new_id = new_id.lower()

    # 2. 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자 외 문자 제거
    answer = "".join([c for c in new_id if c.isalnum() or c in "._-"])

    # 3. 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while ".." in answer:
        answer = answer.replace("..", ".")

    # 4. 마침표(.)가 처음이나 끝에 위치한다면 제거
    answer = "".join(answer).strip(".")
    # 5. new_id가 빈 문자열이라면, new_id에 "a"를 대입
    if not answer:
        answer = "a"
    # 6. 길이가 16자 이상이면 15자까지만 사용, 15번째에 마침표는 제거
    if len(answer) > 15:
        answer = answer[:15].rstrip(".")
    # 7. new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 길이가 3이 될 때까지

    while len(answer) < 3:
        answer += answer[-1]

    return answer