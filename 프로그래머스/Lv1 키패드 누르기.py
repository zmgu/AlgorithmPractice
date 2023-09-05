def solution(numbers, hand):
    answer = ''
    
    pad = [
        [3, 1], 
        [0, 0], [0, 1], [0, 2],
        [1, 0], [1, 1], [1, 2],
        [2, 0], [2, 1], [2, 2]
    ]
    
    l = [3, 0]
    r = [3, 2]
    
    for num in numbers:
        if num in (1, 4, 7):
            l = pad[num]
            answer += 'L'
        elif num in (3, 6, 9):
            r = pad[num]
            answer += 'R'
        else:
            r_distance = abs((r[0]-pad[num][0])) + abs((r[1]-pad[num][1]))
            l_distance = abs((l[0]-pad[num][0])) + abs((l[1]-pad[num][1]))
            if l_distance < r_distance:
                l = pad[num]
                answer += 'L'
            elif r_distance < l_distance:
                r = pad[num]
                answer += 'R'
            elif r_distance == l_distance:
                if hand == 'left':
                    l = pad[num]
                    answer += 'L'
                elif hand == 'right':
                    r = pad[num]
                    answer += 'R'

    return answer
