def solution(players, callings):

    rank ={player: idx for idx, player in enumerate(players)}

    for call in callings:
        current = rank[call]
        
        rank[players[current-1]] += 1
        rank[players[current]] -= 1
        
        temp = players[current-1]
        players[current-1] = players[current]
        players[current] = temp
        
    return players
