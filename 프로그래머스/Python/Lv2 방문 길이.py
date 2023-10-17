def solution(dirs):
    xy = [0, 0]
    arr = []
    
    for i in range(len(dirs)):
        xy1 = list(xy)
        
        if dirs[i] == 'U' and xy[1] < 5:
            xy[1] += 1
        elif dirs[i] == 'D' and xy[1] > -5:
            xy[1] -= 1
        elif dirs[i] == 'R'and xy[0] < 5:
            xy[0] += 1
        elif dirs[i] == 'L' and xy[0] > -5:
            xy[0] -= 1
        else:
            continue
        
        move1 = xy1+xy
        move2 = xy+xy1
        
        if move1 in arr or move2 in arr:
            continue
        arr.append(move1)
        
    return len(arr)
