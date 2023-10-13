def solution(arr1, arr2):        
    answer = [[0]*len(arr2[0]) for i in range(len(arr1))]

    for arr1_row in range(0, len(arr1)):
        for arr2_col in range(0, len(arr2[0])):
            hap = 0
            for arr2_row in range(0, len(arr2)):
                hap += arr1[arr1_row][arr2_row] * arr2[arr2_row][arr2_col]
                
            answer[arr1_row][arr2_col] = hap
                        
    return answer
