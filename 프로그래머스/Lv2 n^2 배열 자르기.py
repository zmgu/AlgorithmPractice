# 시간 초과 뜬 나의 코드
def solution(n, left, right):
    answer = []
    no = 1
    arr = [no]*n

    while len(answer) < right:
        for i in range(no,n):
            arr[i] = i+1
        answer += arr
        x = no
        no +=1
        arr = [no if x < no else x for x in arr]
    answer = answer[left:right+1]

    return answer

# 시간 초과를 안나게 할 방법이 잘 떠오르지 않아 다른 사람의 코드를 가져와 확인했다...
# 프로그래머스 유저 SeDo11 님의 코드
def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        v = max(i//n, i%n) + 1 # x=i//n, y=i%n | x, y 중에 큰 수를 구해 +1을 해서 값으로 넣어줌
        answer.append(v)
    return answer
