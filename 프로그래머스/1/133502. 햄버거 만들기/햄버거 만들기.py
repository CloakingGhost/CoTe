def solution(ingredient):
    if len(ingredient) < 3:
        return 0
    
    answer = 0
    
    stack = ingredient[:4]

    for i in ingredient[4:]:
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
            answer += 1
        stack.append(i)
        
    if stack and stack[-4:] == [1, 2, 3, 1]:
        answer += 1
    return answer