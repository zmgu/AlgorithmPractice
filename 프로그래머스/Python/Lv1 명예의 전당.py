def solution(k, score):
    answer = []
    
    s_arr = []
    for i in score:
        if len(s_arr) < k:
            s_arr.append(i)
        else:
            if i > s_arr[0]:
                s_arr[0] = i
        s_arr.sort()
        answer.append(min(s_arr))
    
    return answer
