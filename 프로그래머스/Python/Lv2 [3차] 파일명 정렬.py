def solution(files):
    answer = []
    file = []
    for i in range(len(files)):
        head = ''
        num, num_idx = '', 0
        
        for idx in range(1, len(files[i])):
            if files[i][idx-1].isdigit() == False and files[i][idx].isdigit():
                head = files[i][:idx].upper()
                num_idx = idx
            elif files[i][idx-1].isdigit() and files[i][idx].isdigit() == False:
                num = int(files[i][num_idx:idx])
                break
                
        if num == '':
            num = int(files[i][num_idx:])
        file.append([head, num, i])
    
    file.sort(key=lambda x:x[1])
    file.sort(key=lambda x:x[0])
    
    for f in file:
        answer.append(files[f[2]])
                
    return answer
