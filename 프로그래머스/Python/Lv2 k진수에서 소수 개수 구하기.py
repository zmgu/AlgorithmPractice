def jinsu(n, k):
    arr = []
    while n > 0:
        arr.append(str(n%k))
        n = int(n//k)        
    arr.reverse()
    
    return ''.join(arr)

def prime(n):   
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(2, int(n**0.5)+1):        
            if n%i == 0:
                return 0
    return 1
    
def solution(n, k):
    answer = 0   
    s = jinsu(n, k)
    arr = s.split('0')    
    for i in range(len(arr)):
        if arr[i] != '': 
            answer += prime(int(arr[i]))
    
    return answer
