def solution(food):
    left_player = "".join([str(i) * (amount//2) for i, amount in enumerate(food)])
    right_player = left_player[::-1]
    return left_player + "0" + right_player 