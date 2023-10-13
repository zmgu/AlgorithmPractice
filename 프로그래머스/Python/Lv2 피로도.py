from itertools import permutations

def solution(k, dungeons):
    answer = []
    
    arr = list(permutations(dungeons, len(dungeons)))
    
    for data in arr:
        
        num = int(k)   
        answer_num = 0
        
        for i in range(len(data)):
            
            if num >= data[i][0]:
                
                num -= data[i][1]
                answer_num += 1
                
        answer.append(answer_num)
    
    return max(answer)
