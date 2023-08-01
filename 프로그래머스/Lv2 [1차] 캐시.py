# 정확성 60퍼로 실패한 나의 코드...

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0 :
        return len(cities) * 5        

    cashe_city = ['']*cacheSize
    cashe_use = [0]*cacheSize
    
    for i in range(0, len(cities)):
        city = cities[i].lower()
        
        if city not in cashe_city:
            j = cashe_use.index(min(cashe_use))
            cashe_city.append(city)
            del cashe_city[j]
            cashe_use.append(0)
            del cashe_use[j]          
            answer += 5
        else:
            index_city = cashe_city.index(city)
            cashe_use[index_city] += 1
            answer += 1            
            cashe_city.append(city)
            del cashe_city[index_city]
            cashe_use.append(cashe_use[index_city])
            del cashe_use[index_city]

    return answer

# deque를 활용한 다른 사람의 풀이
from collections import deque

def solution(cacheSize, cities):
    dq = deque(maxlen=cacheSize)
    run_time = 0
    for city in cities:
        city = city.lower()
        if city not in dq: # cache miss
            dq.append(city)
            run_time += 5
        else: # cache hit
            dq.remove(city)
            dq.append(city)
            run_time += 1

    return run_time
