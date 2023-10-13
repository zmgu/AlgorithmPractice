def solution(msg):
    answer = []
    
    words = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    end = 1
    while end <= len(msg):
        if msg[:end] in words:            
            if end >= len(msg):
                answer.append(words.index(msg))
                break
            end += 1
        else:
            words.append(msg[:end])
            answer.append(words.index(msg[:end-1]))
            msg = msg[end-1:]
            end = 1
                
    return answer
