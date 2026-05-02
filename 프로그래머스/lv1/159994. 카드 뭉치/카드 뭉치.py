from collections import deque
def solution(cards1, cards2, goal):
    cards1, cards2 = deque(cards1), deque(cards2)
    for g_card in goal:

        if cards1 and cards1[0] == g_card:
            cards1.popleft()
        elif cards2 and cards2[0] == g_card:
            cards2.popleft()
        else :
            return "No"
        
    return "Yes"