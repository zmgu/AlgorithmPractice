def solution(X, Y):
    x = sorted(X)
    y = sorted(Y)
    pair = []
    x_idx = 0
    y_idx = 0
    
    while x_idx < len(x):
        try:
            if x[x_idx] == y[y_idx]:
                pair.append(x[x_idx])
                x_idx += 1
                y_idx += 1
            elif x[x_idx] > y[y_idx]:
                y_idx += 1
            elif x[x_idx] < y[y_idx]:
                x_idx += 1
        except:
            break
    
    if len(pair) == 0:
        return '-1'
    else: 
        pair.sort(reverse=True)        
        for i in range(len(pair)):
            if pair[i] != '0':
                return ''.join(pair)
        return '0'
