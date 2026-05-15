def solution(wallpaper):
    m, n = len(wallpaper), len(wallpaper[0])
    
    # 상단좌측, 좌측상단, 우측하단, 하단우측
    location: list[tuple[int, int]] = []
    
    isStop = False
    # 상단좌측
    for i in range(m):
        for j in range(n):
            if wallpaper[i][j] == "#":
                location.append((i, j))
                isStop = True
                break
        if isStop:
            isStop = False
            break
    # 좌측상단
    for i in range(n):
        for j in range(m):
            if wallpaper[j][i] == "#":
                location.append((j, i))
                isStop = True
                break
        if isStop:
            isStop = False
            break
    # 우측하단
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if wallpaper[i][j] == "#":
                location.append((i, j))
                isStop = True
                break
        if isStop:
            isStop = False
            break
    # 하단우측
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if wallpaper[j][i] == "#":
                location.append((j, i))
                isStop = True
                break
        if isStop:
            isStop = False
            break
        
    # 시작점, 끝점
    s = [min(location[0][0], location[1][0]), min(location[0][1], location[1][1])]
    e = [
        max(location[2][0], location[3][0]) + 1,
        max(location[2][1], location[3][1]) + 1,
    ]

    return s + e