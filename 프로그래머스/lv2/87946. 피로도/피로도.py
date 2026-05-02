def solution(k, dungeons):
    total_dungeons = len(dungeons)

    visited = [0] * total_dungeons
    ans = -1
    def perm(depth, tired):
        nonlocal ans
        ans = max(depth, ans)
        
        for i in range(total_dungeons):
            if not visited[i] and  tired>= dungeons[i][0]:
                visited[i] = 1
                perm(depth+1, tired- dungeons[i][1])
                visited[i] = 0
                
    perm(0, k)
        
    return ans