def solution(want, number, discount):
    answer = 0
    
    dic = dict()
    for i in range(10):
        try:
            dic[discount[i]] += 1
        except:
            dic[discount[i]] = 1
            
    wan = dict()
    for i in range(len(want)):
        wan[want[i]] = number[i]
    
    for i in range(10, len(discount)):

        if wan == dic:
            answer += 1
        try:
            dic[discount[i-10]] -= 1
            if dic[discount[i-10]] == 0:
                del dic[discount[i-10]]
            dic[discount[i]] += 1
        except:
            dic[discount[i]] = 1
            continue
            
    if wan == dic:
        answer += 1
    return answer
