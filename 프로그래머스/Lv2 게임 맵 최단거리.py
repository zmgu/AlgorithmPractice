def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [1, 0, -1, 0]  # 오른쪽, 아래, 왼쪽, 위 순서로 이동
    dy = [0, 1, 0, -1]
    
    queue = [(0, 0, 1)]  # (x, y, 이동 횟수)를 저장하는 큐
    
    while queue:
        x, y, move = queue.pop(0)
        
        if x == m - 1 and y == n - 1:  # 목표 위치에 도달한 경우
            return move
        
        for i in range(4):  # 4방향 이동을 시도
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] = 0  # 방문한 위치를 표시
                queue.append((nx, ny, move + 1))
    
    return -1  # 도달할 수 없는 경우

