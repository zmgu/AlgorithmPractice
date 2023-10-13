def solution(ingredient):
    answer = 0
    
    if len(ingredient) < 4:
        return 0
    
    arr = list(ingredient[:3])
    ai = 3

    for i in range(3, len(ingredient)):
        if len(arr) >= 3:
            if arr[ai-3] == 1 and arr[ai-2] == 2 and arr[ai-1] == 3 and ingredient[i] == 1:
                answer += 1
                arr.pop()
                arr.pop()
                arr.pop()
                ai -= 3
                continue        
        arr.append(ingredient[i])
        ai += 1

    return answer
