def check(s):
    ck = []
    i = 0
    while i<len(s):
        if s[i] in ('(','[','{'):
            ck.append(s[i])
        else:
            if len(ck) == 0:
                return 0
            else:
                if ck[-1] == '(' and s[i] == ')':
                    ck.pop()
                elif ck[-1] == '[' and s[i] == ']':
                    ck.pop()
                elif ck[-1] == '{' and s[i] == '}':
                    ck.pop()
                else:
                    return 0
        if len(ck) == 0 and i == len(s)-1:
            return 1
        i += 1

def solution(s):
    answer = 0
    i = 0
    if len(s)%2 !=0:
        return 0
    while i<len(s):
        answer += check(s)
        s = s[1:] + s[0]
        i +=1

    return answer