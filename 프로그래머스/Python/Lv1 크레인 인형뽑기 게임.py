def solution(board, moves):
    answer = 0

    arr = []
    
    for x in moves:
        x -= 1
        for y in range(len(board)):
            if board[y][x] != 0:
                if len(arr) == 0:
                    arr.append(board[y][x])
                elif arr[-1] == board[y][x]:
                    arr.pop()
                    answer += 2
                else:
                    arr.append(board[y][x])
                board[y][x] = 0
                break
                       
    return answer
