def solution(skill, skill_trees):
    answer = 0
    
    s = list(skill)
    skills ={sk: idx for idx, sk in enumerate(s)}
    
    for i in range(len(skill_trees)):
        ck = []
        boolean = True
        
        for j in range(len(skill_trees[i])):
            if skill_trees[i][j] in skills:
                if len(ck) == 0:
                    if skills[skill_trees[i][j]] == 0:
                        ck.append(skills[skill_trees[i][j]])
                    else:
                        boolean = False
                        break
                else:
                    if skills[skill_trees[i][j]] == ck[-1]+1:
                        ck.append(skills[skill_trees[i][j]])
                    else:
                        boolean = False
                        break 
                        
        if boolean is True:
            answer += 1
    
    return answer
