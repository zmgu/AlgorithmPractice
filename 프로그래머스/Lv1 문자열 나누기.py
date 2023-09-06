def solution(s):
    answer = 0
    
    x = ''
    x_cnt = 0  
    y_cnt = 0
    
    for i in range(len(s)):
        if i == len(s)-1:
            answer += 1
            break
            
        if x == '':
            x = s[i]
            x_cnt = 1
            continue

        if s[i] == x:
            x_cnt += 1            
        elif s[i] != x:
            y_cnt += 1
            
            if x_cnt == y_cnt:
                answer += 1
                x = ''                    
                y_cnt = 0
        
    return answer
