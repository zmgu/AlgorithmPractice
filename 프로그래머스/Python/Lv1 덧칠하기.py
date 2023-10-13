def solution(n, m, section):
    answer = 1
    ck = section[0]
    for i in range(1 ,len(section)):
        if ck+m-1 < section[i]:
            answer += 1
            ck = section[i]
            
    return answer
