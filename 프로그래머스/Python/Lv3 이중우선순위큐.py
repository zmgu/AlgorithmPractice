def solution(operations):
    answer = []
    
    h = []
    
    for op in operations:
        try:
            if op == 'D 1':
                h.remove(max(h))
            elif op == 'D -1':
                h.remove(min(h))
            else:
                num = int(op[2:])
                h.append(num)
        except:
            continue
    
    if len(h) == 0:
        answer = [0, 0]
    else:        
        answer = [max(h), min(h)]
    
    return answer
