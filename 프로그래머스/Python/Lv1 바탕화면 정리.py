def solution(wallpaper):
    answer = []
    max_y = 0
    max_x = 0
    min_x = 0
    
    for i in range(len(wallpaper)):
        if '#' in wallpaper[i]:
            if max_y == 0:
                answer.append(i)
            max_y = i+1
            
            for j in range(len(wallpaper[i])):
                if wallpaper[i][j] == '#':
                    temp = j
                    if j == 0:
                        min_x = -1
                    elif j != 0 and min_x == 0 and max_x == 0:
                        min_x = j
                        max_x = j
                    if temp < min_x:
                        min_x = temp
                    elif temp > max_x:
                        max_x = temp
                    print(min_x)
    if min_x == -1:
        answer.append(0)
    else:
        answer.append(min_x)               
    answer.append(max_y)
    answer.append(max_x+1)
    
    return answer
