def solution(a, b, n):
    answer = 0
    while n >= a:
        quotient = n // a * b
        remainder = n % a
        answer += quotient
        n = remainder + quotient

    return answer

