def solution(lottos, win_nums):
    answer = []
    
    cnt = 0
    zero = lottos.count(0)
    
    lottos.sort()
    
    for i in range(zero, 6):
        if lottos[i] in win_nums:
            cnt += 1
    m = cnt + zero
    if m == 6:
        answer.append(1)
    elif m == 5:
        answer.append(2)
    elif m == 4:
        answer.append(3)
    elif m == 3:
        answer.append(4)
    elif m == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    if cnt == 6:
        answer.append(1)
    elif cnt == 5:
        answer.append(2)
    elif cnt == 4:
        answer.append(3)
    elif cnt == 3:
        answer.append(4)
    elif cnt == 2:
        answer.append(5)
    else:
        answer.append(6)
        
    return answer
