def solution(s):
    qe = ['ckeck => ',s[0]]
    i = 1
    while i <len(s):
        if qe[-1] == s[i]:
            qe.pop()
        else:
            qe.append(s[i])
        i += 1
    answer = len(qe)
    if answer > 1:
        return 0
    else:
        return 1
        
