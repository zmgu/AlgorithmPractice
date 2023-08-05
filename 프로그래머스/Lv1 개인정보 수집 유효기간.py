def solution(today, terms, privacies):
    answer = []
    
    month = 28
    year = month * 12
    
    today = today.split('.')
    int_today = (int(today[0]) * year) + (int(today[1]) * month) + int(today[2])
    
    str_term = ['']*len(terms)
    int_term = [0]*len(terms)
    
    for i in range(0,len(terms)):
        terms[i] = terms[i].split()
        int_term[i] = int(terms[i][1]) * month
        str_term[i] = terms[i][0]
        
    for i in range(0,len(privacies)):
        privacies[i] = privacies[i].split(' ')
        privacies[i][0] = privacies[i][0].split('.')
        int_pr = (int(privacies[i][0][0]) * year) + (int(privacies[i][0][1]) * month) + int(privacies[i][0][2])
        idx_term = str_term.index(privacies[i][1])
        int_pr += int_term[idx_term]
        if int_pr <= int_today:
            answer.append(i+1)
    
    return answer
