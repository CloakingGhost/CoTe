import sys, math

n = int(sys.stdin.readline())


def isPrime(target):
    if target < 2:
        return False
    if target == 2 or target == 3:
        return True
    if target % 2 == 0 or target % 3 == 0:
        return False

    sqrt_target = math.ceil(math.sqrt(target))

    for num in range(5, sqrt_target):
        if target % (num - 1) == 0 or target % (num + 1) == 0:
            return False
    return True


def isPalindrome(number):
    if number < 2:
        return False

    str_num = str(number)
    if str_num == str_num[::-1]:
        return True
    
    return False


for num in range(n, sys.maxsize):
    if isPrime(num) and isPalindrome(num):
        print(num)
        break
