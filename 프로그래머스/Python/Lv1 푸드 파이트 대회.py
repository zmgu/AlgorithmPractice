def solution(food):    
    f, b = '', ''
    
    for i in range(1, len(food)):
        ran = int(food[i]/2)
        for j in range(ran):
            f = f + f'{i}'
            b = f'{i}' + b
    
    answer = f + '0' + b   
    
    return answer
