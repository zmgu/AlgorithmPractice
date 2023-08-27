def solution(new_id):
    answer = ''
    if len(new_id) == 0:
        return 'aaa'
    
    new_id = new_id.lower()
    ck = 'qwertyuiopasdfghjklzxcvbnm-_1234567890'
    
    for i in range(len(new_id)):
        if new_id[i] in ck:
            answer += new_id[i]
        elif new_id[i] == '.':
            if len(answer) == 0:
                continue
            elif answer[-1] != '.':
                answer += new_id[i]
    
    if len(answer) == 0:
        return 'aaa'
    
    if len(answer) > 15:
        answer = answer[:15]                
    
    if answer[-1] == '.':
        answer = answer[:-1]
    
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1]
    
    return answer
