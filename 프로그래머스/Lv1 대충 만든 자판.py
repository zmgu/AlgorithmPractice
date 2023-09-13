def solution(keymap, targets):
    answer = []
    key_dic = dict()
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            key = keymap[i][j]
            if key not in key_dic:
                key_dic[key] = j+1
            elif key_dic[key] > j+1:
                key_dic[key] = j+1
                
    for i in range(len(targets)):
        click = 0       
        for j in range(len(targets[i])):
            key = targets[i][j]
            if key in key_dic:
                click += key_dic[key]
            else:
                click = -1
                break
            
        answer.append(click)
        
    return answer
