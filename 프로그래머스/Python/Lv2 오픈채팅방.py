def solution(record):
    answer = []
    
    uid = dict()
    for r in record:
        check = r.split()
        if check[0] in ('Enter', 'Change'):
            uid[check[1]] = check[2]
    
    for r in record:
        check = r.split()
        if check[0] == 'Enter':
            answer.append(f'{uid[check[1]]}님이 들어왔습니다.')
        elif check[0] == 'Leave':
            answer.append(f'{uid[check[1]]}님이 나갔습니다.')
            
    return answer
