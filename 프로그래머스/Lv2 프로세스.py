from collections import deque

def solution(priorities, location):
    answer = 0

    arr = deque(priorities)
    fi = []
    while len(arr) > 0:
        if arr[0] != max(arr):
            arr.append(arr[0])
            if location == 0:
                location = len(arr)-1
        else:
            fi.append(arr[0])
            if location == 0:
                break
            
        arr.popleft()
        location -= 1
    answer = len(fi)
    
    return answer
