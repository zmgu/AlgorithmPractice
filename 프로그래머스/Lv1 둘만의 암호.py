def solution(s, skip, index):
    answer = ''
    
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    arr += arr+arr
    
    for i in range(len(s)):
        cnt_idx = 0
        idx = arr.index(s[i])
        
        while cnt_idx < index:
            if arr[idx+1] not in skip:              
                cnt_idx += 1
            idx += 1
            
        answer += arr[idx]
    
    return answer
