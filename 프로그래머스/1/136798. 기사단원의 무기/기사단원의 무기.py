def solution(number, limit, power):
    answer = [0 for _ in range(number + 1)]
    for i in range(1, number + 1):

        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                
                answer[i] += 2
                if j * j == i:
                    answer[i] -= 1
                
            if answer[i] > limit:
                answer[i] = power
                break
    
    return sum(answer)