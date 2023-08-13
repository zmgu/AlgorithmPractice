def sdt(num, sdt):
    if sdt == 'D':
        num = num ** 2
    elif sdt == 'T':
        num = num ** 3
    return num

def solution(dartResult):
    if dartResult[1] != '0':
        a1 = sdt(int(dartResult[0]), dartResult[1])
        dartResult = dartResult[2:]
    else:
        a1 = sdt(10, dartResult[2])
        dartResult = dartResult[3:]
        
    if dartResult[0] == '#':
        a1 = a1 * (-1)
        dartResult = dartResult[1:]
    elif dartResult[0] == '*':
        a1 *= 2
        dartResult = dartResult[1:]
    
    if dartResult[1] != '0':
        a2 = sdt(int(dartResult[0]), dartResult[1])
        dartResult = dartResult[2:]
    else:
        a2 = sdt(10, dartResult[2])
        dartResult = dartResult[3:]
            
    if dartResult[0] == '#':
        a2 = a2 * (-1)
        dartResult = dartResult[1:]
    elif dartResult[0] == '*':
        a1 *= 2
        a2 *= 2
        dartResult = dartResult[1:]
    
    if dartResult[1] != '0':
        a3 = sdt(int(dartResult[0]), dartResult[1])
    else:
        a3 = sdt(10, dartResult[2])

    if len(dartResult) == 3:
        if dartResult[2] == '#':
            a3 = a3 * (-1)
        elif dartResult[2] == '*':
            a2 *= 2
            a3 *= 2
    answer = a1 + a2 + a3
        
    return answer
