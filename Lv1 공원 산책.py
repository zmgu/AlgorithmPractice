def solution(park, routes):
    max_x, max_y= len(park[0]), len(park)
    # 시작 위치 찾기
    start = []   
    for i in range(len(park)):
        if 'S' in park[i]:
            start.append(i)            
            start.append(park[i].index('S'))
    # 동서남북
    for i in range(len(routes)):
        move = routes[i].split()
        move[1] = int(move[1])
        y = start[0]
        x = start[1]
        cntX = 0
        # 밑으로
        if move[0] == 'S':
            if (y+move[1]) < max_y:
                for my in range(y+1, (y+move[1])+1):
                    if park[my][x] == 'X':
                        cntX += 1
                if cntX == 0:
                    start[0] += move[1]                    
        # 위로
        elif move[0] == 'N':
            if y-move[1] >= 0:
                for my in range((y-move[1]),y):
                    if park[my][x] == 'X':
                        cntX += 1
                if cntX == 0:
                    start[0] -= move[1]
        # 오른쪽
        elif move[0] == 'E':
            if (x+move[1]) < max_x:
                for mx in range(x+1, (x+move[1])+1):
                    if park[y][mx] == 'X':
                        cntX += 1
                if cntX == 0:
                    start[1] += move[1]
        # 왼쪽
        elif move[0] == 'W':
            if x-move[1] >= 0:
                for mx in range((x-move[1]),x):
                    if park[y][mx] == 'X':
                        cntX += 1
                if cntX == 0:
                    start[1] -= move[1]
    
    return start
