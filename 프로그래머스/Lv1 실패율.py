def solution(N, stages):
    answer = []

    score = {}
    total = len(stages)

    for n in range(1, N + 1):
        if total == 0:
            score[n] = 0
        else:
            n_cnt = stages.count(n)
            score[n] = n_cnt / total
            total -= n_cnt

    sorted_score = sorted(score, key=score.get, reverse=True)

    for stage in sorted_score:
        answer.append(stage)
    
    return answer
