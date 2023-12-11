def solution(bandage, health, attacks):
    answer = 0
    
    end = attacks[-1][0] + 1
    hp = int(health)
    
    attack_cnt = 0
    bandage_cnt = 0
    # 연속 회복
    
    for i in range(1, end):
        
        if i == attacks[attack_cnt][0]:
            hp -= attacks[attack_cnt][1]
            
            if hp < 1:
                return -1
            bandage_cnt = 0
            attack_cnt += 1
        else:
            hp += bandage[1]
            
            if hp > health:
                hp = health
            
            bandage_cnt += 1
            
            if bandage_cnt == bandage[0]:
                hp += bandage[2]
                bandage_cnt = 0
    
    if hp < 1:
        return -1
    else:
        return hp
