def solution(array):
    answer = 0
    dic = dict()
    
    for no in array:
        if no not in dic:
            dic[no] = 1
        else:
            dic[no] += 1
            
    dd = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    answer = dd[0][0]
    if len(dd) >= 2 and dd[0][1] == dd[1][1]:
        answer = -1
        
    return answer
