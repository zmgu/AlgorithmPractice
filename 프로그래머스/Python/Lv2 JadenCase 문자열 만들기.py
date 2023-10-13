def solution(s):
    ups = s.upper()
    s = s.lower()
    answer = ups[0]
    
    for i in range(1,len(s)):
        if s[i-1] == ' ':            
            answer += ups[i]
        else:
            answer += s[i]    
    
    return answer
