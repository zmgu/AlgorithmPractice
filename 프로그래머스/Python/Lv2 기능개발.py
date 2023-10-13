def solution(progresses, speeds):
    days = []
    
    for i in range(len(progresses)):        
        nam = 100 - progresses[i]
        day = 0       
        while nam > 0:
            nam -= speeds[i]
            day += 1
        days.append(day)
        
    answer = [1]
    idx = 0
    day_idx = 0
    
    for i in range(1, len(days)):
        if days[day_idx] >= days[i]:
            answer[idx] += 1
        else:
            answer.append(1)
            idx += 1
            day_idx = i
        
    return answer
