def solution(s):
    answer = []
    arr = [''] * (s.count(',')+1)
    k = 0
    for i in range(2,len(s)-2):
        if s[i] not in ('{', '}', ','):
            arr[k] += s[i]
        elif s[i] == ',':
            k += 1
    set_arr = list(set(arr))
    set_arr.sort()
    cnt_arr = []
    for i in range(0,len(set_arr)):
        cnt_arr.append(arr.count(set_arr[i]))
        
    for i in range(0,len(set_arr)):
        idx = cnt_arr.index(max(cnt_arr))
        answer.append(int(set_arr[idx]))
        cnt_arr[idx] = 0
            
    return answer
