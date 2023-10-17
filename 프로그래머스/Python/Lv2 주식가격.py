def solution(prices):
    a = [0] * len(prices)
    
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            a[i] += 1
            if prices[j] < prices[i]:
                break        
    return a
