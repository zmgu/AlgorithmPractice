# 효율성 테스트를 통과하지 못했던 처음 코드
def solution(people, limit):
    answer = 0
    people.sort()
    while len(people)>1:
        answer +=1
        if people[0]+people[-1] <= limit:
            people.pop(-1)
            people.pop(0)
        else:
            people.pop(-1)
    if len(people) == 1:
        answer +=1
    return answer

# pop을 사용하면 효율성 테스트를 통과하지 못할 것 같아 새롭게 풀이한 코드
def solution(people, limit):
    answer = 0
    people.sort()

    start = 0
    end = len(people)-1

    while start<end:
        if people[start]+people[end] <= limit:
            start += 1
        end -= 1
        if start == end:
            return answer + 2
        answer += 1

    return answer
