from itertools import permutations as pm

def solution(expression):
    answer = []
    
    arr, op = [], []
    s, e = 0, 0
    for i in range(len(expression)):
        if expression[i] in ('-','+','*'):
            arr.append(int(expression[s:e]))
            arr.append(expression[i])
            if expression[i] not in op:
                op.append(expression[i])
            
            s, e = i+1, i+1
        else:
            e += 1
            if e == len(expression):
                arr.append(int(expression[s:]))
    
    rotation = list(pm(op, len(op)))
    
    for ro in rotation:
        i = 0
        copy = list(arr)
        while i < len(ro):
            idx = 1
            while ro[i] in copy:
                if copy[idx] == ro[i]:
                    if ro[i] == '*':
                        copy[idx-1] = copy[idx-1] * copy[idx+1]
                    elif ro[i] == '+':
                        copy[idx-1] = copy[idx-1] + copy[idx+1]
                    else:
                        copy[idx-1] = copy[idx-1] - copy[idx+1]
                        
                    copy.pop(idx)
                    copy.pop(idx)
                    idx = 1
                    
                    if len(copy) == 1:
                        answer.append(abs(copy[0]))
                        break
                    else:
                        continue
                else:
                    idx += 2
            
            i += 1
            
    return max(answer)
