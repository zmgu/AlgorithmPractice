def solution(clothes):
    answer = 1
    dic = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in dic.keys():
            dic[clothes[i][1]] = 2
        else:
            dic[clothes[i][1]] += 1
    for value in dic.values():
        answer *= value
    
    return answer-1
