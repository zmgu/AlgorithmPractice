def solution(brown, yellow):
    i =1
    while True:
        x = (brown-(2*i))/2
        y = 2+i
        if x*y == brown + yellow:
            answer = [x,y]
            break
        else:
            i+=1
    return answer
