from queue import PriorityQueue as pq

def solution(scoville, K):
    answer = 0
    
    s = pq()
    for i in range(len(scoville)):
        s.put(scoville[i])

    while s.qsize() > 1:
        temp = s.get()
        if temp < K:
            s.put(temp+(s.get()*2))
            answer += 1
        else:
            return answer  
    
    if s.queue[0] < K:
        answer = -1
        
    return answer
