from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])
    while queue:
        depth, total = queue.popleft()
        if depth == len(numbers):
            if total == target:
                answer += 1
            continue
        queue.append((depth + 1, total + numbers[depth]))
        queue.append((depth + 1, total - numbers[depth]))
    return answer