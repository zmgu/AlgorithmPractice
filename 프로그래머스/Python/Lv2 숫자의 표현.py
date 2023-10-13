def solution(n):
    if n == 1:
        return 1
    
    answer = 0
    div = 1
    start = int(n/div) - int((div-1)/2)
    
    while start > 1:
        start = int(n/div) - int((div-1)/2)
        sum = 0
        
        for i in range(start, start+div):
            sum += i
            
        if sum == n:
            answer += 1
        div += 1
        
    return answer
