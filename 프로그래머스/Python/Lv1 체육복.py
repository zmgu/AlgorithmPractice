def solution(n, lost, reserve):
    lost.sort()    
    lost1 = list(lost)
    
    for los in lost:
        if los in reserve:
            reserve.remove(los)
            lost1.remove(los)   
            
    lost2 = list(lost1)
    
    for los in lost1:
        if los - 1 in reserve:
            reserve.remove(los-1)
            lost2.remove(los)
            
        elif los + 1 in reserve:
            reserve.remove(los+1)
            lost2.remove(los)
    
    answer = n - len(lost2)
    
    return answer
