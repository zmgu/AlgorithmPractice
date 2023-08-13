def solution(cards1, cards2, goal):
    arr1 = []
    arr2 = []
    
    arr1_ck = False
    arr2_ck = False
    
    for i in range(0,len(goal)):
        if goal[i] in cards1:
            arr1.append(goal[i])
        else:
            arr2.append(goal[i])
            
    for i in range(0, len(arr1)):
        if arr1[i] == cards1[i]:
            arr1_ck = True
        else:
            arr1_ck = False
            
    for i in range(0, len(arr2)):
        if arr2[i] == cards2[i]:
            arr2_ck = True
        else:
            arr2_ck = False
    
    if arr1_ck is True and arr2_ck is True:
        return 'Yes'
    else:
        return 'No'
