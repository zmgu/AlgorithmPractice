def solution(str1, str2):
    answer = 0
    ck_arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    str1, str2 = str1.lower() , str2.lower()

    arr1 = []
    arr2 = []
    for i in range(1,len(str1)):
        if str1[i-1] in ck_arr and str1[i] in ck_arr:
            if i == len(str1)-1:
                ck = str1[i-1:]
            else:
                ck = str1[i-1:i+1]
            arr1.append(ck)
    for i in range(1,len(str2)):
        if str2[i-1] in ck_arr and str2[i] in ck_arr:
            if i == len(str2)-1:
                ck = str2[i-1:]
            else:
                ck = str2[i-1:i+1]
            arr2.append(ck)

    
    if len(arr2) >= len(arr1):
        temp = arr1
        arr1 = arr2
        arr2 = temp
        
    lenarr1 = len(arr1)
    i = 0
    hap = 0
    
    while i<len(arr2):
        if arr2[i] in arr1:
            hap += 1
            arr1.remove(arr2[i])
            arr2.remove(arr2[i])
        else:
            i += 1
    
    
    uni = lenarr1 + len(arr2)
    if hap == 0:
        if uni == 0:
            return 65536
        else:
            return 0
    answer = int((hap/uni)*65536)
    
    return answer
