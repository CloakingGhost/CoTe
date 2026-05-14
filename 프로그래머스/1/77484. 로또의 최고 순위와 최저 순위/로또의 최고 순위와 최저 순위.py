def solution(lottos, win_nums):
    lottos_set, win_nums_set = set(lottos), set(win_nums)
    zero_count = lottos.count(0)

    result =  win_nums_set & lottos_set
    max_rank, min_rank = 0, 0
    
    def get_rank(count):
        return 7 - count if count > 1 else 6

    min_rank = get_rank(len(result))
    max_rank = get_rank(len(result) + zero_count)


    
    return [max_rank, min_rank]