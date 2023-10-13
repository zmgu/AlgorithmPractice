def solution(n, words):
    answer = []
    number = 2
    fi = []
    fi.append(words[0])
    rounds = 1
    for i in range(1,len(words)):
        if words[i-1][-1] == words[i][0]:
            if words[i] not in fi:
                fi.append(words[i])
                number += 1
                if number == n+1:
                    number = 1
                    rounds +=1
            else:
                answer.append(number)
                answer.append(rounds)                
                return answer
        else:
            answer.append(number)
            answer.append(rounds)                
            return answer
    answer.append(0)
    answer.append(0)
    return answer

            
