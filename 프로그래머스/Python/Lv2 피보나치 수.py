def solution(n):
    f1 = 0
    f2 = 1
    answer = 0
    i = 1
    
    while i<=n-1:
        answer = f1 + f2
        f1 = f2
        f2 = answer
        i+=1
    answer = answer%1234567
    return answer
