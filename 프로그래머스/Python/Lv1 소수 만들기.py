def solution(nums):
    answer = 0
    num = len(nums)
    for i in range(0, num-2):
        j = i + 1
        for j in range(i+1, num-1):
            k = j + 1
            for k in range(j + 1, num):
                hap = nums[i] + nums[j] + nums[k]
                pr_ck = 0
                for pr in range(1, hap + 1):
                    if hap%pr == 0:
                        pr_ck += 1
                if pr_ck == 2:
                    answer += 1
    return answer
