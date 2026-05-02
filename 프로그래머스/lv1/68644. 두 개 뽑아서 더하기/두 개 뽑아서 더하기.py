def loop(numList, ans):
    if len(numList) < 2:
        return ans
    
    first = numList[0]
    rest = numList[1:]
    for num in rest:
        ans.add(first + num)
    
    return loop(rest, ans)
        
def solution(numbers):
    
    return sorted(list(loop(numbers, set())))