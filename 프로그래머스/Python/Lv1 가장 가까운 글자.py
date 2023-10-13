def solution(s):
    answer = []
    ck = []
    idx = []
    for i in range(0,len(s)):
        if s[i] not in ck:
            ck.append(s[i])
            idx.append(i)
            answer.append(-1)
        else:

            answer.append(i-idx[ck.index(s[i])])
            idx[ck.index(s[i])] = i
            
    return answer
