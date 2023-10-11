def solution(x):
    strx = str(x)
    sum = 0
    for i in range(len(strx)):
        sum += int(strx[i])
    
    if x%sum == 0:
        return True
    else:
        return False
