def solution(k, tangerine):
    maxt = max(tangerine)
    arr = [0]*maxt
    for i in range(0,len(tangerine)):
        arr[tangerine[i]-1] += 1
    arr.sort(reverse =True)
    sum = 0
    answer = 0
    for i in range(0,len(arr)):
        sum += arr[i]
        answer +=1
        if sum >= k:
            return answer

    return answer