def solution(id_list, report, k):
    answer = [0]*len(id_list)
    
    report = list(set(report))

    arr = [[''] for i in range(len(id_list))]
    
    for i in range(0, len(report)):            
        ids = report[i].split(" ")
        id_idx = id_list.index(ids[1])
        arr[id_idx].append(ids[0])
    
    for i in range(0, len(arr)):
        if len(arr[i]) >= k+1:
            for j in arr[i][1:]:
                id_idx = id_list.index(j)
                answer[id_idx] += 1

    return answer
